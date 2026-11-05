"""Starter Tkinter sales explorer for the course pack.

Run from the repository root: python examples/sales_explorer.py
The application is a teaching MVP. It loads data in the UI thread; for large or remote sources,
use the background-worker pattern described in Chapter 17.
"""
from __future__ import annotations

from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd

try:
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
except ImportError:  # Charts are optional; file/table functionality still works.
    Figure = None
    FigureCanvasTkAgg = None

COLUMNS = ["order_id", "order_date", "customer_id", "region", "product", "category", "quantity", "unit_price", "unit_cost", "status"]
DISPLAY_COLUMNS = ["order_id", "order_date", "region", "customer_id", "product", "category", "quantity", "revenue", "profit", "status"]


def load_frame(path: Path) -> pd.DataFrame:
    suffix = path.suffix.lower()
    selected_sheet = None
    if suffix == ".csv":
        raw = pd.read_csv(path, dtype={"order_id": "string", "customer_id": "string"}, low_memory=False)
    elif suffix in {".xlsx", ".xlsm"}:
        # Workbooks may start with a summary sheet. Choose the first sheet that matches
        # the canonical line-level schema instead of blindly reading sheet zero.
        workbook = pd.ExcelFile(path)
        selected_sheet = None
        for candidate in workbook.sheet_names:
            header = pd.read_excel(workbook, sheet_name=candidate, nrows=0)
            normalized = {str(c).strip().lower().replace(" ", "_") for c in header.columns}
            if set(COLUMNS).issubset(normalized):
                selected_sheet = candidate
                break
        if selected_sheet is None:
            raise ValueError("No worksheet contains the required sales-line columns. Choose a sheet with order_id, order_date, customer_id, region, product, category, quantity, unit_price, unit_cost, and status.")
        raw = pd.read_excel(workbook, sheet_name=selected_sheet, dtype={"order_id": "string", "customer_id": "string"})
    else:
        raise ValueError("Choose a .csv, .xlsx, or .xlsm file.")
    raw.columns = [str(c).strip().lower().replace(" ", "_") for c in raw.columns]
    missing = set(COLUMNS) - set(raw.columns)
    if missing:
        raise ValueError(f"The file is missing required columns: {', '.join(sorted(missing))}")
    frame = raw.copy()
    frame["order_date"] = pd.to_datetime(frame["order_date"], errors="coerce")
    for column in ("quantity", "unit_price", "unit_cost"):
        frame[column] = pd.to_numeric(frame[column], errors="coerce")
    frame["revenue"] = frame["quantity"] * frame["unit_price"]
    frame["cost"] = frame["quantity"] * frame["unit_cost"]
    frame["profit"] = frame["revenue"] - frame["cost"]
    frame.attrs["source_sheet"] = selected_sheet
    return frame


class SalesExplorer:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Tkinter Sales Analytics Explorer")
        self.root.geometry("1180x760")
        self.root.minsize(860, 560)
        self.raw = pd.DataFrame()
        self.filtered = pd.DataFrame()
        self.source_path: Path | None = None
        self.page = 0
        self.page_size = 100
        self.sort_by = "order_date"
        self.sort_reverse = True
        self.region = tk.StringVar(value="All")
        self.category = tk.StringVar(value="All")
        self.status_filter = tk.StringVar(value="All")
        self.status = tk.StringVar(value="Open a sales CSV or Excel workbook")
        self.kpi_text = {
            "rows": tk.StringVar(value="Lines\n—"),
            "orders": tk.StringVar(value="Orders\n—"),
            "revenue": tk.StringVar(value="Revenue\n—"),
            "profit": tk.StringVar(value="Profit\n—"),
            "margin": tk.StringVar(value="Margin\n—"),
        }
        self._build_ui()
        self._load_default_sample()

    def _build_ui(self) -> None:
        self.root.rowconfigure(2, weight=1)
        self.root.columnconfigure(0, weight=1)
        toolbar = ttk.Frame(self.root, padding=8)
        toolbar.grid(row=0, column=0, sticky="ew")
        for label, command in (("Open file…", self.open_file), ("Export CSV…", self.export_csv), ("Export Excel…", self.export_excel), ("Reset filters", self.reset_filters)):
            ttk.Button(toolbar, text=label, command=command).pack(side="left", padx=3)

        filters = ttk.LabelFrame(self.root, text="Filters", padding=8)
        filters.grid(row=1, column=0, sticky="ew", padx=8, pady=(0, 8))
        for col in range(6):
            filters.columnconfigure(col, weight=1 if col in (1, 3, 5) else 0)
        ttk.Label(filters, text="Region").grid(row=0, column=0, sticky="w", padx=4, pady=4)
        self.region_box = ttk.Combobox(filters, textvariable=self.region, state="readonly", values=["All"], width=14)
        self.region_box.grid(row=0, column=1, sticky="ew", padx=4, pady=4)
        ttk.Label(filters, text="Category").grid(row=0, column=2, sticky="w", padx=4, pady=4)
        self.category_box = ttk.Combobox(filters, textvariable=self.category, state="readonly", values=["All"], width=16)
        self.category_box.grid(row=0, column=3, sticky="ew", padx=4, pady=4)
        ttk.Label(filters, text="Status").grid(row=0, column=4, sticky="w", padx=4, pady=4)
        self.status_box = ttk.Combobox(filters, textvariable=self.status_filter, state="readonly", values=["All"], width=14)
        self.status_box.grid(row=0, column=5, sticky="ew", padx=4, pady=4)
        ttk.Button(filters, text="Apply", command=self.apply_filters).grid(row=0, column=6, padx=4, pady=4)

        kpis = ttk.Frame(self.root, padding=(8, 0, 8, 8))
        kpis.grid(row=2, column=0, sticky="nsew")
        kpis.columnconfigure(0, weight=1)
        kpis.rowconfigure(1, weight=1)
        cards = ttk.Frame(kpis)
        cards.grid(row=0, column=0, sticky="ew", pady=(0, 8))
        for i, key in enumerate(self.kpi_text):
            cards.columnconfigure(i, weight=1)
            ttk.Label(cards, textvariable=self.kpi_text[key], relief="groove", padding=8, anchor="center").grid(row=0, column=i, sticky="ew", padx=3)

        body = ttk.Panedwindow(kpis, orient="vertical")
        body.grid(row=1, column=0, sticky="nsew")
        table_frame = ttk.Frame(body, padding=2)
        chart_frame = ttk.Frame(body, padding=4)
        body.add(table_frame, weight=3)
        body.add(chart_frame, weight=2)
        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)
        self.table = ttk.Treeview(table_frame, columns=DISPLAY_COLUMNS, show="headings", height=12)
        for col in DISPLAY_COLUMNS:
            self.table.heading(col, text=col.replace("_", " ").title(), command=lambda c=col: self.sort_table(c))
            self.table.column(col, width=105 if col not in ("product", "category") else 135, minwidth=70, anchor="w")
        yscroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        xscroll = ttk.Scrollbar(table_frame, orient="horizontal", command=self.table.xview)
        self.table.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
        self.table.grid(row=0, column=0, sticky="nsew")
        yscroll.grid(row=0, column=1, sticky="ns")
        xscroll.grid(row=1, column=0, sticky="ew")
        pager = ttk.Frame(table_frame)
        pager.grid(row=2, column=0, columnspan=2, sticky="ew", pady=4)
        self.page_label = ttk.Label(pager, text="Page —")
        self.page_label.pack(side="left", padx=6)
        ttk.Button(pager, text="Previous", command=self.previous_page).pack(side="right", padx=3)
        ttk.Button(pager, text="Next", command=self.next_page).pack(side="right", padx=3)

        self.chart_label = ttk.Label(chart_frame, text="Chart unavailable: install Matplotlib to enable it.")
        self.chart_label.pack(fill="both", expand=True)
        self.figure = None
        self.ax = None
        self.canvas = None
        if Figure is not None and FigureCanvasTkAgg is not None:
            self.figure = Figure(figsize=(7, 2.5), dpi=90, constrained_layout=True)
            self.ax = self.figure.add_subplot(111)
            self.canvas = FigureCanvasTkAgg(self.figure, master=chart_frame)
            self.canvas.get_tk_widget().pack(fill="both", expand=True)
            self.chart_label.destroy()
        ttk.Label(self.root, textvariable=self.status, anchor="w", relief="sunken", padding=(6, 4)).grid(row=3, column=0, sticky="ew")

    def _load_default_sample(self) -> None:
        candidate = Path(__file__).resolve().parents[1] / "data" / "sample_sales.csv"
        if candidate.exists():
            try:
                self.set_dataset(load_frame(candidate), candidate)
            except Exception as exc:
                self.status.set(f"Sample load failed: {exc}")

    def open_file(self) -> None:
        selected = filedialog.askopenfilename(
            parent=self.root,
            title="Open sales dataset",
            filetypes=[("CSV and Excel", "*.csv *.xlsx *.xlsm"), ("CSV", "*.csv"), ("Excel", "*.xlsx *.xlsm"), ("All files", "*.*")],
        )
        if not selected:
            self.status.set("Open cancelled; current data retained")
            return
        path = Path(selected)
        try:
            frame = load_frame(path)
        except (OSError, ValueError, UnicodeError, pd.errors.ParserError, ImportError) as exc:
            messagebox.showerror("Could not load dataset", str(exc), parent=self.root)
            self.status.set(f"Load failed: {path.name}; previous data retained")
            return
        self.set_dataset(frame, path)

    def set_dataset(self, frame: pd.DataFrame, path: Path | None) -> None:
        self.raw = frame
        self.source_path = path
        self.region_box.configure(values=["All"] + sorted(frame["region"].dropna().astype(str).unique().tolist()))
        self.category_box.configure(values=["All"] + sorted(frame["category"].dropna().astype(str).unique().tolist()))
        self.status_box.configure(values=["All"] + sorted(frame["status"].dropna().astype(str).unique().tolist()))
        self.region.set("All")
        self.category.set("All")
        self.status_filter.set("All")
        self.page = 0
        self.apply_filters()
        sheet_label = f" · sheet {frame.attrs['source_sheet']}" if frame.attrs.get("source_sheet") else ""
        self.status.set(f"Loaded {len(frame):,} order lines from {path.name if path else 'memory'}{sheet_label}")

    def apply_filters(self) -> None:
        if self.raw.empty:
            self.filtered = self.raw.copy()
        else:
            frame = self.raw
            if self.region.get() != "All":
                frame = frame[frame["region"].astype(str).eq(self.region.get())]
            if self.category.get() != "All":
                frame = frame[frame["category"].astype(str).eq(self.category.get())]
            if self.status_filter.get() != "All":
                frame = frame[frame["status"].astype(str).eq(self.status_filter.get())]
            self.filtered = frame.copy()
        self.page = 0
        revenue = float(self.filtered["revenue"].sum()) if not self.filtered.empty else 0.0
        profit = float(self.filtered["profit"].sum()) if not self.filtered.empty else 0.0
        orders = int(self.filtered["order_id"].nunique()) if not self.filtered.empty else 0
        margin = profit / revenue if revenue else None
        self.kpi_text["rows"].set(f"Lines\n{len(self.filtered):,}")
        self.kpi_text["orders"].set(f"Orders\n{orders:,}")
        self.kpi_text["revenue"].set(f"Revenue\n{revenue:,.2f}")
        self.kpi_text["profit"].set(f"Profit\n{profit:,.2f}")
        self.kpi_text["margin"].set(f"Margin\n{margin:.1%}" if margin is not None else "Margin\n—")
        self.render_table()
        self.render_chart()
        self.status.set(f"Showing {len(self.filtered):,} matching order lines")

    def render_table(self) -> None:
        self.table.delete(*self.table.get_children())
        if self.filtered.empty:
            self.page_label.configure(text="No matching rows")
            return
        ordered = self.filtered.sort_values(self.sort_by, ascending=not self.sort_reverse, na_position="last")
        pages = max(1, (len(ordered) + self.page_size - 1) // self.page_size)
        self.page = min(self.page, pages - 1)
        page_frame = ordered.iloc[self.page * self.page_size:(self.page + 1) * self.page_size]
        for idx, row in page_frame.iterrows():
            values = []
            for col in DISPLAY_COLUMNS:
                value = row.get(col, "")
                if pd.isna(value):
                    value = ""
                elif col in ("unit_price", "unit_cost", "revenue", "profit"):
                    value = f"{float(value):,.2f}"
                elif col == "order_date":
                    value = pd.Timestamp(value).strftime("%Y-%m-%d") if value != "" else ""
                values.append(value)
            self.table.insert("", "end", iid=str(idx), values=values)
        self.page_label.configure(text=f"Page {self.page + 1} of {pages} · {len(self.filtered):,} matches · {self.page_size} rows/page max")

    def sort_table(self, column: str) -> None:
        if column not in self.filtered.columns:
            return
        if self.sort_by == column:
            self.sort_reverse = not self.sort_reverse
        else:
            self.sort_by = column
            self.sort_reverse = False
        self.render_table()

    def previous_page(self) -> None:
        if self.page > 0:
            self.page -= 1
            self.render_table()

    def next_page(self) -> None:
        if not self.filtered.empty and (self.page + 1) * self.page_size < len(self.filtered):
            self.page += 1
            self.render_table()

    def reset_filters(self) -> None:
        self.region.set("All")
        self.category.set("All")
        self.status_filter.set("All")
        self.apply_filters()

    def render_chart(self) -> None:
        if self.ax is None or self.canvas is None:
            return
        self.ax.clear()
        if self.filtered.empty or self.filtered["order_date"].isna().all():
            self.ax.text(0.5, 0.5, "No valid dates for the current filters", ha="center", va="center", transform=self.ax.transAxes)
            self.ax.set_axis_off()
        else:
            valid = self.filtered.dropna(subset=["order_date"]).copy()
            valid["month"] = valid["order_date"].dt.to_period("M").astype(str)
            monthly = valid.groupby("month", as_index=False)["revenue"].sum().sort_values("month")
            self.ax.bar(monthly["month"], monthly["revenue"])
            self.ax.set_title("Revenue by month")
            self.ax.set_ylabel("Revenue (illustrative currency units)")
            self.ax.tick_params(axis="x", rotation=35, labelsize=8)
            self.ax.grid(axis="y", alpha=0.25)
        self.canvas.draw_idle()

    def export_csv(self) -> None:
        if self.filtered.empty:
            messagebox.showinfo("Nothing to export", "The current filters contain no rows.", parent=self.root)
            return
        name = "filtered_sales.csv"
        path = filedialog.asksaveasfilename(parent=self.root, title="Export filtered rows", defaultextension=".csv", initialfile=name, filetypes=[("CSV", "*.csv")])
        if not path:
            self.status.set("CSV export cancelled")
            return
        destination = Path(path)
        if destination.exists() and not messagebox.askyesno("Overwrite file?", f"Replace {destination.name}?", parent=self.root):
            self.status.set("CSV export cancelled; existing file retained")
            return
        try:
            self.filtered.to_csv(destination, index=False, encoding="utf-8")
        except OSError as exc:
            messagebox.showerror("Export failed", str(exc), parent=self.root)
            self.status.set("CSV export failed")
            return
        self.status.set(f"Exported {len(self.filtered):,} filtered rows to {destination.name}")

    def export_excel(self) -> None:
        if self.filtered.empty:
            messagebox.showinfo("Nothing to export", "The current filters contain no rows.", parent=self.root)
            return
        path = filedialog.asksaveasfilename(parent=self.root, title="Export Excel report", defaultextension=".xlsx", initialfile="sales_report.xlsx", filetypes=[("Excel workbook", "*.xlsx")])
        if not path:
            self.status.set("Excel export cancelled")
            return
        destination = Path(path)
        if destination.exists() and not messagebox.askyesno("Overwrite file?", f"Replace {destination.name}?", parent=self.root):
            self.status.set("Excel export cancelled; existing file retained")
            return
        summary = pd.DataFrame([{
            "line_count": len(self.filtered),
            "unique_orders": int(self.filtered["order_id"].nunique()),
            "unique_customers": int(self.filtered["customer_id"].nunique()),
            "revenue": float(self.filtered["revenue"].sum()),
            "profit": float(self.filtered["profit"].sum()),
            "region_filter": self.region.get(),
            "category_filter": self.category.get(),
            "status_filter": self.status_filter.get(),
            "source": str(self.source_path) if self.source_path else "memory",
        }])
        quality = pd.DataFrame({"column": self.filtered.columns, "dtype": [str(self.filtered[c].dtype) for c in self.filtered.columns], "missing_count": [int(self.filtered[c].isna().sum()) for c in self.filtered.columns]})
        try:
            with pd.ExcelWriter(destination, engine="openpyxl") as writer:
                summary.to_excel(writer, sheet_name="Summary", index=False)
                self.filtered.to_excel(writer, sheet_name="Filtered Data", index=False)
                quality.to_excel(writer, sheet_name="Data Quality", index=False)
        except (OSError, ImportError, ValueError) as exc:
            messagebox.showerror("Excel export failed", str(exc), parent=self.root)
            self.status.set("Excel export failed")
            return
        self.status.set(f"Exported Excel report to {destination.name}")


def main() -> None:
    root = tk.Tk()
    SalesExplorer(root)
    root.mainloop()


if __name__ == "__main__":
    main()
