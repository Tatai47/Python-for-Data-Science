# Python Data Analysis and Visualization — Beginner to Advanced

This book contains **19 chapter folders and 57 Jupyter notebooks**. Each chapter has a theory notebook, a guided tutorial, and a practical lab. The style is deliberately theory-heavy while retaining runnable examples and exercises.

## Start here
1. Install Python 3.10+.
2. Create and activate a virtual environment.
3. Install core packages: `pip install -r requirements-core.txt`.
4. Open `START_HERE.ipynb` in JupyterLab or Jupyter Notebook.
5. Read `BOOK_OUTLINE.md`, then work through each chapter's three notebooks in order.

## Recommended setup
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements-core.txt
jupyter lab
```

Install `requirements-full.txt` for optional packages used in extended examples. Some optional tools, such as MySQL Server, are external services and are not installed by pip.

## Contents
- `BOOK_OUTLINE.md` — full syllabus, chapter goals, section allocation, and learning path.
- `START_HERE.ipynb` — orientation and how to use this book.
- `Chapter_01_...` through `Chapter_19_...` — three notebooks per chapter plus a chapter-specific outline.
- `data/` — synthetic CSV and JSON data used throughout.
- `requirements-core.txt` / `requirements-full.txt` — dependencies.
- `PROJECT_ROADMAP.md` — suggested portfolio projects.

## Data and privacy
All included datasets are synthetic teaching data. Do not paste production credentials into notebooks. Use environment variables or an appropriate secret manager for database/API secrets.

## MySQL note
The database chapters use SQLite as a no-server fallback so SQL lessons can execute immediately. To connect to MySQL, install and start a MySQL server separately, create a database/user, install `mysql-connector-python`, and configure `MYSQL_HOST`, `MYSQL_PORT`, `MYSQL_USER`, `MYSQL_PASSWORD`, and `MYSQL_DATABASE` environment variables. Use parameterized queries and least-privilege accounts.

## Notebook execution
Run each chapter in order from its folder or from the project root. The notebook setup cells locate the bundled `data/` directory relative to the project. Execute notebooks from a clean kernel before relying on saved state. Some interactive chart outputs render best in JupyterLab.

## License and attribution
The prose and synthetic examples in this learning pack are original educational material. The notebooks link to official documentation for the third-party tools; consult their licenses and documentation for current API details.

## Sample outputs
`sample_outputs/` contains example CSV, JSON, Excel, PNG, and SVG files produced by selected exercises. These are reference artifacts; the notebooks remain the source of truth and can regenerate them.

## Validation note
The package includes saved text outputs and 24 inline PNG chart previews. All 58 notebooks passed notebook-format validation, all Python code cells passed syntax validation, and all 265 code cells executed successfully in isolated Python notebook-style namespaces during package validation. Optional libraries are guarded or identified as optional; a live MySQL server is not included.
