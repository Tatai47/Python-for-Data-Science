# Chapter 06 — Pandas I: Series, DataFrames, and Inspection

**Purpose:** Pandas makes labelled, heterogeneous tabular data easier to inspect and manipulate. Focus on the data model, selection, indexing, dtypes, and descriptive summaries.

**Prerequisites:** Python and NumPy basics; install Pandas.

## Learning goals
- Explain Series, DataFrame, index, columns, and alignment.
- Read tabular data and inspect its structure.
- Select rows and columns with loc and iloc.
- Understand dtypes, missing values, and descriptive summaries.

## Topic and subtopic plan
### 1. Series and DataFrame
A `Series` is a one-dimensional labelled array with an index. A `DataFrame` is a two-dimensional labelled table whose columns may have different dtypes. Useful attributes: `.index`, `.columns`, `.dtypes`, `.shape`, `.ndim`, `.size`, `.empty`. Attributes do not use parentheses; methods such as `.head()` do. Keep column labels unique.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 2. Reading tabular data
`pd.read_csv(filepath_or_buffer, sep=",", header="infer", names=None, index_col=None, usecols=None, dtype=None, parse_dates=None, na_values=None, encoding=None)` reads delimited text. `usecols` reduces columns, `dtype` controls type inference, `parse_dates` converts date fields, `na_values` adds missing markers. Other readers include `read_json`, `read_excel`, `read_parquet`, and `read_sql`.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 3. Selection and indexing
`df["column"]` selects a Series; `df[["a","b"]]` selects multiple columns. `.loc[row_label, column_label]` is label-based; `.iloc[row_position, column_position]` is integer-position-based. `.loc` label slices include endpoint labels; `.iloc` follows Python-exclusive stop behavior. Use `.loc[mask, columns]` for explicit conditional selection and assignment.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 4. Data types and index design
Common dtypes: `int64`, `float64`, `bool`, `object`, `string`, `category`, and `datetime64`. Nullable extension dtypes (`Int64`, `boolean`, `string`) can represent missing values. An index labels rows but is not automatically a primary key. `set_index` and `reset_index` move values between columns and index; `astype` converts validated types; `to_datetime(errors="coerce")` turns invalid dates into `NaT`.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 5. First-pass inspection
`head(n=5)`, `tail(n=5)`, `info()`, `describe(include=..., exclude=...)`, `value_counts(dropna=True)`, `nunique(dropna=True)`, `isna`, and `notna` are core inspection methods. Numeric summaries do not prove data quality; separately validate ranges, allowed categories, uniqueness, dates, and foreign keys.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

## Material allocation
| Notebook | Approximate effort | Coverage |
|---|---:|---|
| Concepts and Theory | 45–75 min | All subtopics, terminology, parameter reference, function variations, limitations, demonstrations. |
| Step-by-Step Tutorial | 45–75 min | Guided 1 — Establish the shape; Guided 2 — Filter a region; Guided 3 — Summarize numeric columns; Guided 4 — Compute profit margin |
| Practical Lab and Exercises | 60–120 min | Scenario, tasks, worked reference solution, and an extension challenge. |

## Practical lab brief
Perform an initial analysis of sales data. Establish the row grain, identify data types, select a regional subset, and compute a margin metric.

### Required tasks
- Load sales.csv and inspect shape, info, and preview.
- Classify numeric, categorical, identifier, and date columns.
- Select North region orders with loc.
- Calculate row-level profit margin and total weighted margin.

### Extension challenge
Explain why a DataFrame row index is not a stable business key. Demonstrate after sorting and filtering.

### References
- Pandas getting started: https://pandas.pydata.org/docs/getting_started/index.html
- Pandas user guide: https://pandas.pydata.org/docs/user_guide/index.html
