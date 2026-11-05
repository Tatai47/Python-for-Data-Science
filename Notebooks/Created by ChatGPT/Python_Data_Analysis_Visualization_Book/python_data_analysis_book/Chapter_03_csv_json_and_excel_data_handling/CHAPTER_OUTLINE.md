# Chapter 03 — CSV, JSON, and Excel Data Handling

**Purpose:** Files are common boundaries between systems. Learn text encoding, CSV delimiters and quoting, JSON objects and arrays, Excel workbooks, and robust import/export patterns.

**Prerequisites:** Python file handling and basic DataFrame concepts.

## Learning goals
- Read and write CSV with the standard library and Pandas.
- Parse JSON objects and arrays and understand serialization options.
- Import/export Excel workbooks with Pandas and OpenPyXL.
- Handle encodings, missing values, and data types.

## Topic and subtopic plan
### 1. CSV structure and standard-library API
CSV is a text interchange format, not a database; it has no universal type system. Fields use a delimiter and may be quoted to protect embedded delimiters/newlines. `csv.reader` yields lists; `DictReader` maps fields to header names; `writer` and `DictWriter` export rows. Important options include `delimiter`, `quotechar`, `escapechar`, `fieldnames`, `restkey`, `restval`, `encoding`, and `newline=""` when writing.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 2. JSON data model
JSON supports objects, arrays, strings, numbers, booleans, and null. `json.load(file)`/`loads(text)` parse; `dump(obj,file)`/`dumps(obj)` serialize. Options: `indent` controls pretty formatting; `sort_keys` stabilizes key order; `ensure_ascii=False` preserves readable Unicode; `separators` controls whitespace; `default=` converts otherwise unsupported objects; `allow_nan=False` rejects non-standard NaN/Infinity. JSON object keys are strings.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 3. Excel workbooks
An `.xlsx` workbook contains sheets, cells, formulas, formatting, and other workbook objects. `pd.read_excel(io, sheet_name=0, header=0, usecols=None, dtype=None, skiprows=None, nrows=None, engine=None)` returns a DataFrame or a dict when `sheet_name=None`. `to_excel` exports a frame; `ExcelWriter` writes multiple sheets. OpenPyXL is useful for cell-level styles, formulas, dimensions, and charts.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 4. Pandas CSV import parameters
`read_csv` options commonly used: `sep`, `header`, `names`, `index_col`, `usecols`, `dtype`, `parse_dates`, `na_values`, `keep_default_na`, `encoding`, `encoding_errors`, `decimal`, `thousands`, `skiprows`, `nrows`, and `on_bad_lines`. Choose `dtype` for IDs and `parse_dates` for timestamps. Inspect inferred types after import.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 5. Data contracts and export choices
Blanks, `NA`, `N/A`, and zero can have different meanings. Validate required columns and expected types. CSV is widely interoperable; JSON handles nested records; Excel is convenient for formatted multi-sheet handoffs. Preserve raw files and document how missing markers, date formats, and decimal separators are handled.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

## Material allocation
| Notebook | Approximate effort | Coverage |
|---|---:|---|
| Concepts and Theory | 45–75 min | All subtopics, terminology, parameter reference, function variations, limitations, demonstrations. |
| Step-by-Step Tutorial | 45–75 min | Guided 1 — Validate CSV columns; Guided 2 — Load JSON; Guided 3 — Select and export data; Guided 4 — Create Excel sheets |
| Practical Lab and Exercises | 60–120 min | Scenario, tasks, worked reference solution, and an extension challenge. |

## Practical lab brief
Build a file-processing pipeline that reads CSV and JSON, validates columns, creates a regional report, and exports CSV, JSON, and Excel deliverables.

### Required tasks
- Read sales.csv with a string order ID and parsed date.
- Load weather.json into a DataFrame.
- Check required columns and unique IDs.
- Export a regional summary to CSV, JSON, and a two-sheet Excel workbook.

### Extension challenge
Add duplicate detection, invalid-date reporting, and negative-revenue checks. Compare file sizes and explain the trade-off between CSV and JSON.

### References
- Python csv: https://docs.python.org/3/library/csv.html
- Python json: https://docs.python.org/3/library/json.html
- Pandas IO: https://pandas.pydata.org/docs/user_guide/io.html
- OpenPyXL: https://openpyxl.readthedocs.io/
