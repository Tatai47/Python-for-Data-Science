# Chapter 16 — Exploratory Data Analysis and Data Quality

**Purpose:** Exploratory data analysis (EDA) combines data contracts, missingness analysis, outlier investigation, distributions, relationships, and communication. It turns a raw dataset into a defensible analytical starting point.

**Prerequisites:** Pandas, NumPy, basic plotting, and introductory statistics.

## Learning goals
- Define grain, keys, and quality rules before analyzing.
- Profile missingness, duplicates, types, ranges, and categories.
- Investigate outliers without blindly deleting them.
- Explore univariate and multivariate structure.
- Create a reproducible EDA summary and communicate caveats.

## Topic and subtopic plan
### 1. Data grain and data contracts
Grain states what one row represents (for example, one order line or one customer). Define primary keys, candidate keys, required fields, allowed categories, units, date ranges, and relationships. A duplicate row may be an error or a valid repeated event; uniqueness must be defined at the correct grain. Validate assumptions explicitly with assertions or schema libraries.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 2. Missingness
`isna()` identifies missing values; `notna()` identifies present values; `isna().mean()` gives missing proportion. Missing completely at random, missing at random, and missing not at random are conceptual mechanisms, not conclusions available from a missingness heatmap alone. Distinguish not applicable, not collected, unknown, and true zero. Imputation can create bias if its assumptions are wrong.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 3. Duplicates, types, and ranges
Use `duplicated(subset=..., keep=...)`, `drop_duplicates`, `to_datetime(errors="coerce")`, `to_numeric(errors="coerce")`, and `.astype(...)`. Validate ranges and category domains. Coercion converts invalid strings to missing; count and review these conversions rather than silently accepting them.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 4. Outliers and robust summaries
Outliers may indicate data errors, rare valid events, or a different population. Investigate source records and units. IQR fences are exploratory flags, not universal deletion rules. Compare mean with median and standard deviation with IQR/MAD. Winsorization and trimming change the estimand and should be justified and documented.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 5. Automated profiling
YData Profiling can create a rich HTML report with types, distributions, correlations, missingness, and warnings. The report is a discovery aid, not a substitute for domain review. Large datasets can generate slow or overly verbose reports; sample carefully and preserve privacy.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 6. Communicating an EDA
A useful handoff states the dataset source, time period, grain, row/column count, key quality findings, transformations, metrics, notable patterns, limitations, and next questions. Separate findings from hypotheses and label exploratory patterns as such.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

## Material allocation
| Notebook | Approximate effort | Coverage |
|---|---:|---|
| Concepts and Theory | 45–75 min | All subtopics, terminology, parameter reference, function variations, limitations, demonstrations. |
| Step-by-Step Tutorial | 45–75 min | Guided 1 — State the grain and key; Guided 2 — Quantify missingness; Guided 3 — Clean text and numeric fields; Guided 4 — Review rather than auto-delete outliers |
| Practical Lab and Exercises | 60–120 min | Scenario, tasks, worked reference solution, and an extension challenge. |

## Practical lab brief
Produce a reproducible EDA and data-quality report for the intentionally messy sales dataset. Do not silently discard records or impute values without justification.

### Required tasks
- Describe the data grain and expected key.
- Report missingness and duplicate counts.
- Parse dates and numeric fields and count coercion failures.
- Normalize text columns while retaining a raw copy.
- Flag IQR outliers and inspect source rows.
- Summarize at least three findings and three limitations.

### Extension challenge
Create a data validation function that checks required columns, key uniqueness, accepted category values, numeric ranges, and date parse success. Return a structured list of errors and warnings rather than stopping at the first issue.

### References
- Pandas missing data: https://pandas.pydata.org/docs/user_guide/missing_data.html
- YData Profiling: https://docs.profiling.ydata.ai/
