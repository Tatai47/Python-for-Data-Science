# Chapter 07 — Pandas II: Cleaning, Transformation, and Aggregation

**Purpose:** Real datasets are rarely analysis-ready. Learn missing-value handling, duplicate detection, strings, dates, grouping, joins, and reshaping.

**Prerequisites:** Chapter 6 DataFrame selection, dtypes, and inspection.

## Learning goals
- Diagnose missing values and duplicates.
- Use string, datetime, and categorical accessors.
- Transform with vectorized operations, map, and apply.
- Group, aggregate, merge, concatenate, pivot, and melt.

## Topic and subtopic plan
### 1. Missing values
Pandas uses `np.nan`, `pd.NA`, and `NaT`. Use `isna`/`notna` for detection. `dropna(axis=0, how="any", subset=None, thresh=None)` removes rows/columns based on missingness. `fillna(value, limit=...)` accepts scalar, mapping, Series, or DataFrame values. Forward/backward filling is meaningful only when row order has temporal meaning. Decide whether missingness itself carries information.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 2. Duplicates and strings
`duplicated(subset=None, keep="first")` marks duplicate rows; `keep="last"` marks earlier copies; `keep=False` marks all members. `drop_duplicates(subset=None, keep="first", ignore_index=False)` removes duplicates. Define identity using business keys. The `.str` accessor includes `strip`, `lower`, `upper`, `replace`, `contains`, `startswith`, `len`, and `extract`; use `na=` where supported.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 3. Dates and times
`pd.to_datetime(arg, errors="raise", utc=False, format=None)` parses timestamps. `errors="coerce"` turns invalid values into `NaT`. `.dt` exposes year, month, day, quarter, and day name. `dt.to_period("M")` produces monthly periods; `dt.floor("D")` rounds down. Set a consistent timezone policy; UTC normalization may require local conversion for reporting.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 4. GroupBy and aggregation
`groupby(by, as_index=True, sort=True, dropna=True)` splits rows into groups. `.agg()` computes summaries; `.transform()` returns an aligned result; `.filter()` retains groups. Named aggregation such as `revenue_total=("revenue","sum")` gives stable names. Prefer built-in operations over Python `apply` where possible.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 5. Merge and concat
`pd.merge(left,right,how="inner",on=None,left_on=None,right_on=None,suffixes=("_x","_y"),validate=None,indicator=False)` joins relational keys. `inner`, `left`, `right`, and `outer` have different retention rules. `validate` can assert one-to-one, one-to-many, or many-to-one. `pd.concat(objs,axis=0,join="outer",ignore_index=False,keys=None)` stacks along rows or columns; use merge for keyed joins and concat for stacking.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 6. Reshaping
`pivot(index,columns,values)` requires unique key combinations. `pivot_table` aggregates duplicates and supports `aggfunc`, `fill_value`, and `margins`. `melt(id_vars,value_vars,var_name,value_name)` converts wide values to long form. Tidy/long data is convenient for plotting and statistical modeling.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

## Material allocation
| Notebook | Approximate effort | Coverage |
|---|---:|---|
| Concepts and Theory | 45–75 min | All subtopics, terminology, parameter reference, function variations, limitations, demonstrations. |
| Step-by-Step Tutorial | 45–75 min | Guided 1 — Preserve raw inputs; Guided 2 — Standardize and handle nulls; Guided 3 — Aggregate and rank; Guided 4 — Validate a customer join |
| Practical Lab and Exercises | 60–120 min | Scenario, tasks, worked reference solution, and an extension challenge. |

## Practical lab brief
Clean a deliberately messy sales extract, create regional summaries, and join customer context without unintentionally multiplying rows.

### Required tasks
- Measure missing values and duplicate order IDs before cleaning.
- Standardize product and region strings.
- Choose a documented missing-value rule.
- Aggregate revenue and profit by region.
- Join orders to customers and validate row count and match status.

### Extension challenge
Build a month-by-region pivot and a rolling three-month metric. Explain why sorting and missing-period policy are essential.

### References
- Missing data: https://pandas.pydata.org/docs/user_guide/missing_data.html
- GroupBy guide: https://pandas.pydata.org/docs/user_guide/groupby.html
- Merge guide: https://pandas.pydata.org/docs/user_guide/merging.html
