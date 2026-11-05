from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def test_sample_sales_schema_and_row_count():
    frame = pd.read_csv(ROOT / "data" / "sample_sales.csv")
    assert len(frame) >= 900
    assert {"order_id", "order_date", "customer_id", "region", "quantity", "unit_price", "unit_cost", "status"}.issubset(frame.columns)
    assert frame["order_id"].notna().all()


def test_sales_rows_have_multiple_orders_or_lines():
    frame = pd.read_csv(ROOT / "data" / "sample_sales.csv")
    assert frame["order_id"].nunique() <= len(frame)
    assert frame["region"].nunique() >= 4


def test_quality_sample_has_known_issues():
    frame = pd.read_csv(ROOT / "data" / "sales_with_issues.csv")
    assert len(frame) > 100
    assert frame["order_date"].astype(str).str.contains("not-a-date").any()
    assert frame["unit_price"].astype(str).str.contains("bad-price").any()
