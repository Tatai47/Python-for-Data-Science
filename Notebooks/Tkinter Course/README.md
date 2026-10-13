# Python Tkinter for Data Analytics — Complete Course Pack

This repository is the companion material for a book-length, notebook-first course on Python Tkinter and data analytics. It contains a master notebook, **40 individual chapter notebooks**, synthetic data, SQL/MongoDB setup examples, and a runnable starter sales explorer.

## Start here

1. Open `Tkinter_Data_Analytics_Master_Book.ipynb` for the full course manuscript, or open `chapters/` and work through the individual chapter notebooks.
2. Use a local desktop Python/Jupyter environment. Tkinter creates native desktop windows; a headless or hosted notebook may not have a display server.
3. Read `requirements.txt` and install only the packages needed for the chapters you are studying. Core Tkinter examples use Python’s standard library; analytics and database chapters use optional packages.
4. Run GUI cells one at a time and close their windows before moving on. **Do not run every cell in the entire master book sequentially**: many examples are interactive, some write files, and database examples require explicit configuration.
5. Start with `data/sample_sales.csv`. The data is synthetic. `data/sales_with_issues.csv` intentionally contains malformed and inconsistent values for quality exercises. If available, `data/sample_sales_workbook.xlsx` contains Summary, Sales Lines, and Data Dictionary sheets.
6. Run the starter application from the project root with `python examples/sales_explorer.py`.

## Book architecture

The planned editorial allocation is approximately 300 pages, with code listings, diagrams, screenshots, labs, review questions, and capstone material. Actual page count depends on trim size, font, line spacing, and how many annotated screenshots/figures are added. Each chapter notebook includes outcomes, lesson notes, worked code examples, a guided lab, review prompts, and further reading.

## Recommended setup

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m tkinter
```

`python -m tkinter` is a quick display/Tk support check. The exact package requirements vary by operating system and Python distribution. A missing Tkinter module is normally resolved by installing a Python build with Tcl/Tk support, not by relying on `pip install tkinter`.

## Optional database integrations

- Copy `.env.example` to `.env` for local development and fill in appropriate settings. Never commit `.env`; the project `.gitignore` excludes it. The notebooks intentionally do not load a production database on import.
- MySQL examples use a least-privilege account and parameterized SQL. Run `sql/mysql_schema.sql` only against a database you control.
- MongoDB examples use PyMongo; `scripts/mongo_setup.js` shows a sample collection shape. Do not run destructive commands against production data.
- A desktop executable cannot keep privileged DB credentials secret. For a real multi-user product, consider a trusted backend service rather than embedding credentials in client code.

## Folder guide

- `chapters/` — independent chapter notebooks
- `data/` — deterministic synthetic data and workbook
- `examples/` — starter desktop application
- `sql/` — relational schema
- `scripts/` — MongoDB sample setup notes
- `tests/` — starter validation tests
- `requirements.txt` — course dependencies (database drivers and other extensions are optional at runtime)
- `course_map.md` — sequence, page budget, and learning outcomes

## Editorial notes

The examples are teaching references and should be reviewed against the installed package/server versions before commercial or institutional publication. Metric definitions, source schemas, security policies, and database behavior are described explicitly where they affect results. The synthetic CSV represents **one row per order line**: an `order_id` can repeat, so count unique orders when the metric calls for order count.
