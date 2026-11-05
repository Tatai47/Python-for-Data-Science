import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Sales Analysis", layout="wide")
st.title("Sales Analysis Dashboard")
DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "sales.csv"

@st.cache_data(ttl=300)
def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path, parse_dates=["order_date"])

sales = load_data(str(DATA_PATH))
regions = st.sidebar.multiselect("Region", sorted(sales.region.unique()), default=sorted(sales.region.unique()))
products = st.sidebar.multiselect("Product", sorted(sales["product"].unique()), default=sorted(sales["product"].unique()))
filtered = sales[sales.region.isin(regions) & sales["product"].isin(products)]

c1, c2, c3 = st.columns(3)
c1.metric("Orders", f"{filtered.order_id.nunique():,}")
c2.metric("Revenue", f"{filtered.revenue.sum():,.0f}")
c3.metric("Profit", f"{filtered.profit.sum():,.0f}")

left, right = st.columns(2)
left.subheader("Revenue by region")
left.bar_chart(filtered.groupby("region").revenue.sum())
right.subheader("Daily revenue")
right.line_chart(filtered.groupby("order_date").revenue.sum())

st.subheader("Filtered orders")
st.dataframe(filtered, use_container_width=True)
st.download_button("Download filtered CSV", filtered.to_csv(index=False).encode("utf-8"), "filtered_sales.csv", "text/csv")
