# Python Data Analysis and Visualization — Complete Book Outline

**Audience:** beginner to advanced.  **Teaching emphasis:** theory-heavy, with executable demonstrations and practical work.

## How the book is structured
Every chapter contains three notebooks built around the same chapter outcomes:
1. **Concepts and Theory** — terminology, mental models, function signatures, arguments, parameters, data types, important variations, edge cases, limitations, and short executable demonstrations.
2. **Step-by-Step Tutorial** — a guided sequence with explanatory commentary, code cells, expected outputs saved in the notebook, and checkpoints.
3. **Practical Lab and Exercises** — a realistic scenario, tasks, a worked reference solution, extension challenges, and references.

## Suggested study time
- Concepts and Theory: 45–75 minutes per chapter.
- Step-by-Step Tutorial: 45–75 minutes per chapter.
- Practical Lab and Exercises: 60–120 minutes per chapter.
- Suggested total: approximately 3–4.5 hours per chapter; more for the database, machine-learning, and capstone chapters.
- Complete all exercises before viewing the reference solution in the lab notebook.

## Chapter-by-chapter syllabus
### Chapter 01 — Python Foundations for Data Work
**Folder:** `Chapter_01_python_foundations_for_data_work/`
**Purpose:** Python is the programming layer underneath the data stack. Learn the language features needed to read data, transform values, automate work, and write reliable scripts.
**Prerequisites:** No previous programming experience; Python 3.10+ recommended.
**Learning goals:**
- Distinguish names, objects, values, and types.
- Choose appropriate built-in data structures.
- Use control flow, comprehensions, and functions for data tasks.
- Handle errors and organize reusable code.
**Section allocation and coverage:**
1. **Names, objects, and types** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. A name refers to an object. Assignment binds a name to an object; it does not copy it. Python is dynamically typed. Core scalar types are `int`, `float`, `bool`, `str`, and `NoneType`. `type(x)` reports an exact type; `isinstance(x, T)` also recognizes subclasses. `True == 1` is true, although `type(True) is int` is false.…
2. **Mutable and immutable objects** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Immutable examples include numbers, strings, and tuples; mutable examples include lists, dictionaries, and sets. `b = a` creates another reference. `a.copy()` makes a shallow copy; nested mutable objects remain shared. `copy.deepcopy()` recursively copies nested objects and may be costly.…
3. **Containers and operations** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Lists are ordered and mutable; tuples are ordered and immutable; dictionaries map hashable keys to values; sets contain unique hashable values. `append(x)` adds one list item; `extend(iterable)` adds many. `dict.get(key, default)` avoids `KeyError`. `set.add` and `set.update` add one and many values respectively.…
4. **Control flow and comprehensions** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `if/elif/else` select branches. `for` traverses an iterable; `while` repeats while a condition is true. `break`, `continue`, and `pass` control loops. List comprehensions use `[expression for item in iterable if condition]`; dictionary and set comprehensions use braces. Prefer a loop when branching or side effects become complex.…
5. **Functions and arguments** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `def f(required, optional=default, *args, **kwargs)` supports positional, defaulted, variable-length positional, and keyword arguments. `/` marks positional-only parameters; `*` marks keyword-only parameters. Avoid mutable defaults. A function without `return` returns `None`. Pass inputs explicitly and return results rather than depending on global variables.…
6. **Errors, files, and modules** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Use narrow `try/except` blocks and catch exceptions you can handle. `else` runs on success; `finally` runs during cleanup. Prefer `pathlib.Path` and context-managed files. Split reusable code into modules; `if __name__ == "__main__":` separates script execution from imports.…
**Notebook allocation:**
- Concepts and Theory: all section explanations plus concise demonstrations.
- Step-by-Step Tutorial: Guided 1 — Summarize a list; Guided 2 — Pair sequences; Guided 3 — Validate inputs; Guided 4 — Work safely with files.
- Practical Lab: Build a reusable student-mark report. Validate the sequence, calculate summary statistics, count passes, and return the top three marks.
**Practical tasks:**
- Write `summarise_marks(marks, pass_mark=40)`.
- Reject empty inputs and non-numeric values.
- Return count, average, highest, lowest, pass_count, and top_three.
- Test one edge case as well as the default case.
**Extension:** Add a keyword-only `round_to` argument and an optional minimum-score filter. Test empty input, text input, a single mark, and values exactly at the pass threshold.
**Core references:** Python tutorial: https://docs.python.org/3/tutorial/ | Built-in functions: https://docs.python.org/3/library/functions.html | Pathlib: https://docs.python.org/3/library/pathlib.html

### Chapter 02 — Jupyter Notebook and Reproducible Workflows
**Folder:** `Chapter_02_jupyter_notebook_and_reproducible_workflows/`
**Purpose:** Jupyter combines narrative, executable code, and saved outputs. Good notebook practice makes an analysis understandable, repeatable, reviewable, and shareable.
**Prerequisites:** Chapter 1 Python fundamentals; JupyterLab or Jupyter Notebook.
**Learning goals:**
- Explain kernels, cells, execution order, and notebook metadata.
- Use Markdown, code cells, magic commands, and rich display.
- Restart and run notebooks from a clean state.
- Control randomness and document dependencies.
**Section allocation and coverage:**
1. **Notebook architecture** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. An `.ipynb` notebook is a JSON document with ordered cells, metadata, and outputs. A kernel is the process that executes code and retains variables. Visible order and execution order can differ; `In [n]` records execution sequence. A cell that depends on hidden state may work only after a particular sequence of clicks. Restart and run all cells before sharing.…
2. **Cell types and outputs** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Code cells execute code; Markdown cells contain headings, prose, tables, links, and math; raw cells are passed through for specialized exporters. Outputs can be text streams, execution results, or rich display data (HTML, images, charts). `print()` creates text; a final expression is usually displayed automatically.…
3. **IPython and magic commands** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. IPython adds `%time`, `%timeit`, `%run`, `%pwd`, `%matplotlib inline`, `%%time`, and `%%writefile`. Magics are an interactive IPython feature, not Python syntax in a regular `.py` file. `%timeit` repeats a short expression; one timing is not a reliable performance benchmark.…
4. **Reproducibility** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Record data source, assumptions, environment, and random seeds. `np.random.default_rng(seed)` gives a reproducible generator in a fixed compatible environment; a seed does not guarantee identical results across all library versions. Prefer project-relative paths, lock dependencies for production, and keep credentials outside notebooks.…
5. **Professional notebook structure** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Use: question and decision context; data description and grain; assumptions; imports/configuration; validation; analysis sections; conclusions/caveats; references. Keep one idea per cell, limit huge outputs, avoid hard-coded secrets, and move reusable functions into modules. Test with a clean kernel.…
**Notebook allocation:**
- Concepts and Theory: all section explanations plus concise demonstrations.
- Step-by-Step Tutorial: Guided 1 — Ask an analytical question; Guided 2 — Inspect the result; Guided 3 — Summarize and rank; Guided 4 — Write a defensible conclusion.
- Practical Lab: Create a clean-kernel notebook analysis answering which region generated the highest sales revenue. Document data checks, metric definition, and a defensible conclusion.
**Practical tasks:**
- Load the sales dataset using a project-relative path.
- Check row count, duplicate IDs, missing values, and date range.
- Summarize revenue by region.
- State one limitation and distinguish observation from explanation.
**Extension:** Export an executive summary to Markdown and compare total revenue with average revenue per order. Re-run after restarting the kernel.
**Core references:** Jupyter documentation: https://docs.jupyter.org/ | IPython documentation: https://ipython.readthedocs.io/

### Chapter 03 — CSV, JSON, and Excel Data Handling
**Folder:** `Chapter_03_csv_json_and_excel_data_handling/`
**Purpose:** Files are common boundaries between systems. Learn text encoding, CSV delimiters and quoting, JSON objects and arrays, Excel workbooks, and robust import/export patterns.
**Prerequisites:** Python file handling and basic DataFrame concepts.
**Learning goals:**
- Read and write CSV with the standard library and Pandas.
- Parse JSON objects and arrays and understand serialization options.
- Import/export Excel workbooks with Pandas and OpenPyXL.
- Handle encodings, missing values, and data types.
**Section allocation and coverage:**
1. **CSV structure and standard-library API** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. CSV is a text interchange format, not a database; it has no universal type system. Fields use a delimiter and may be quoted to protect embedded delimiters/newlines. `csv.reader` yields lists; `DictReader` maps fields to header names; `writer` and `DictWriter` export rows. Important options include `delimiter`, `quotechar`, `escapechar`, `fieldnames`, `restkey`, `restval`, `encoding`, and `newline=""` when writing.…
2. **JSON data model** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. JSON supports objects, arrays, strings, numbers, booleans, and null. `json.load(file)`/`loads(text)` parse; `dump(obj,file)`/`dumps(obj)` serialize. Options: `indent` controls pretty formatting; `sort_keys` stabilizes key order; `ensure_ascii=False` preserves readable Unicode; `separators` controls whitespace; `default=` converts otherwise unsupported objects; `allow_nan=False` rejects non-standard NaN/Infinity. JSON…
3. **Excel workbooks** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. An `.xlsx` workbook contains sheets, cells, formulas, formatting, and other workbook objects. `pd.read_excel(io, sheet_name=0, header=0, usecols=None, dtype=None, skiprows=None, nrows=None, engine=None)` returns a DataFrame or a dict when `sheet_name=None`. `to_excel` exports a frame; `ExcelWriter` writes multiple sheets. OpenPyXL is useful for cell-level styles, formulas, dimensions, and charts.…
4. **Pandas CSV import parameters** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `read_csv` options commonly used: `sep`, `header`, `names`, `index_col`, `usecols`, `dtype`, `parse_dates`, `na_values`, `keep_default_na`, `encoding`, `encoding_errors`, `decimal`, `thousands`, `skiprows`, `nrows`, and `on_bad_lines`. Choose `dtype` for IDs and `parse_dates` for timestamps. Inspect inferred types after import.…
5. **Data contracts and export choices** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Blanks, `NA`, `N/A`, and zero can have different meanings. Validate required columns and expected types. CSV is widely interoperable; JSON handles nested records; Excel is convenient for formatted multi-sheet handoffs. Preserve raw files and document how missing markers, date formats, and decimal separators are handled.…
**Notebook allocation:**
- Concepts and Theory: all section explanations plus concise demonstrations.
- Step-by-Step Tutorial: Guided 1 — Validate CSV columns; Guided 2 — Load JSON; Guided 3 — Select and export data; Guided 4 — Create Excel sheets.
- Practical Lab: Build a file-processing pipeline that reads CSV and JSON, validates columns, creates a regional report, and exports CSV, JSON, and Excel deliverables.
**Practical tasks:**
- Read sales.csv with a string order ID and parsed date.
- Load weather.json into a DataFrame.
- Check required columns and unique IDs.
- Export a regional summary to CSV, JSON, and a two-sheet Excel workbook.
**Extension:** Add duplicate detection, invalid-date reporting, and negative-revenue checks. Compare file sizes and explain the trade-off between CSV and JSON.
**Core references:** Python csv: https://docs.python.org/3/library/csv.html | Python json: https://docs.python.org/3/library/json.html | Pandas IO: https://pandas.pydata.org/docs/user_guide/io.html | OpenPyXL: https://openpyxl.readthedocs.io/

### Chapter 04 — APIs, Web Data, and Schema Validation
**Folder:** `Chapter_04_apis_web_data_and_schema_validation/`
**Purpose:** External systems expose data through HTTP APIs or web pages. Learn HTTP request structure, JSON response handling, defensive parsing, HTML extraction, and schema validation.
**Prerequisites:** Dictionaries, JSON, exceptions, and basic DataFrames; live internet access is optional.
**Learning goals:**
- Explain URLs, methods, status codes, headers, query parameters, and timeouts.
- Use Requests to retrieve and check API responses.
- Parse HTML locally with BeautifulSoup.
- Validate records with Pydantic and report malformed data.
**Section allocation and coverage:**
1. **HTTP and REST** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. An HTTP request combines a method (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`), URL, headers, optional query parameters, and sometimes a body. Responses carry status codes, headers, and content. `2xx` means success; `3xx` redirection; `4xx` client-side issue; `5xx` server-side issue. REST-style APIs model resources, but actual APIs differ: check authentication, pagination, rate limits, and terms.…
2. **Requests API and arguments** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `requests.get(url, params=None, headers=None, timeout=None, auth=None, verify=True, allow_redirects=True)` sends a GET. `params` encodes query parameters; `headers` sends metadata; `timeout` bounds waits; `verify=True` validates TLS certificates and should normally stay enabled. Inspect `status_code`, `headers`, `text`, `content`; use `.json()` for JSON and `.raise_for_status()` for unsuccessful HTTP responses.…
3. **Error handling and retries** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Set timeouts. Catch `Timeout`, `ConnectionError`, and `HTTPError` separately when recovery differs. Respect `Retry-After` for rate limits; bound retries and use backoff for transient failures. Do not retry non-idempotent writes blindly. Validate response shape before loading it into an analytical table. Never log tokens or passwords.…
4. **BeautifulSoup** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `BeautifulSoup(markup, "html.parser")` parses HTML. `find` returns the first match; `find_all` returns all matches; CSS selectors use `.select` and `.select_one`. `.get_text(separator=" ", strip=True)` extracts clean text; `.get("href")` reads an attribute. Prefer documented APIs; respect site policies and minimize requests.…
5. **Pydantic contracts** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Pydantic models validate records using type annotations. `BaseModel` declares fields; `Field(gt=0, min_length=1, ...)` adds constraints. Validation errors identify invalid fields and reasons. Choose whether invalid data stops a job, is quarantined, or is corrected under an explicit rule. Pydantic v2 uses `model_validate`; `parse_obj` is a common v1/v2 compatibility path but deprecated in v2.…
**Notebook allocation:**
- Concepts and Theory: all section explanations plus concise demonstrations.
- Step-by-Step Tutorial: Guided 1 — Inspect the response envelope; Guided 2 — Parse the HTML catalogue; Guided 3 — Validate with Pydantic; Guided 4 — Build a defensive HTTP function.
- Practical Lab: Build a local ingestion pipeline that reads an API-shaped JSON fixture, parses an HTML catalogue, validates products, and creates a clean DataFrame.
**Practical tasks:**
- Check the JSON response status and record count.
- Extract products with a CSS selector from the provided HTML.
- Define positive-price and non-empty-name validation.
- Separate valid and invalid records.
- Explain how a live API function should handle timeout and HTTP errors.
**Extension:** Add a paginated API workflow using `next_page` tokens. Respect retry-after headers and do not retry schema-validation failures as network errors.
**Core references:** Requests: https://requests.readthedocs.io/ | BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/ | Pydantic: https://docs.pydantic.dev/

### Chapter 05 — NumPy: Numerical Computing
**Folder:** `Chapter_05_numpy_numerical_computing/`
**Purpose:** NumPy provides homogeneous n-dimensional arrays and fast vectorized operations, forming the numerical foundation of the Python data ecosystem.
**Prerequisites:** Python lists, loops, functions, and arithmetic; install NumPy.
**Learning goals:**
- Explain ndarray shape, axes, dtype, and memory layout.
- Create, index, slice, reshape, and combine arrays.
- Use broadcasting, vectorized expressions, reductions, and masks.
- Handle missing numeric values and reproducible random sampling.
**Section allocation and coverage:**
1. **The ndarray model** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. A NumPy `ndarray` is a homogeneous n-dimensional array. Key attributes: `ndim`, `shape`, `size`, `dtype`, and `itemsize`. Homogeneous storage enables efficient numerical operations. A 1-D array has one axis; a 2-D array is commonly rows and columns. Numeric dtypes include signed/unsigned integers, floats, complex values, booleans, datetime/timedelta, and strings.…
2. **Array creation** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `np.array(object, dtype=None)` builds from array-like data. `zeros(shape)`, `ones(shape)`, and `full(shape, fill_value)` initialize arrays. `arange(start, stop, step)` builds a step-based range; `linspace(start, stop, num=50, endpoint=True)` creates a fixed number of evenly spaced values. `eye(N, M=None, k=0)` creates an identity-like matrix. Prefer `linspace` if the point count matters.…
3. **Indexing, slicing, and views** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Use `a[row, column]`; `a[:, 1]` selects a column. Slice stop is exclusive. Basic slices usually make views that share memory; advanced integer/boolean indexing usually returns copies. Use `.copy()` for independent values. Boolean masks select elements; combine comparisons with `&` and `|`, parenthesizing each condition. Do not use Python `and/or` on arrays.…
4. **Shape changes and broadcasting** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `reshape` changes shape while preserving element order; `-1` infers one dimension. `ravel()` returns a view where possible; `flatten()` copies. `.T` transposes 2-D arrays. `concatenate` joins along an existing axis; `stack` adds a new axis. Broadcasting compares trailing dimensions: they are compatible when equal or one is 1. `(n,1)` plus `(1,m)` yields `(n,m)`.…
5. **Vectorization and reductions** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Vectorization applies operations to whole arrays instead of Python loops. Reductions include `sum`, `mean`, `min`, `max`, and `std`; `axis=0` reduces rows, yielding per-column results; `axis=1` yields per-row results. `keepdims=True` preserves singleton dimensions for broadcasting. Prefer `np.random.default_rng(seed)`; methods include `integers`, `normal`, `random`, and `choice`.…
6. **Missing values and precision** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `np.nan` is a floating-point missing sentinel; NaN is unequal to itself. Use `isnan`, `nanmean`, and `nanmedian`. Integers cannot normally store NaN without changing dtype. Choose dtypes based on value range and precision requirements; floating point has finite precision, so avoid exact equality tests for computed decimal results.…
**Notebook allocation:**
- Concepts and Theory: all section explanations plus concise demonstrations.
- Step-by-Step Tutorial: Guided 1 — Create a mark matrix; Guided 2 — Calculate along the correct axis; Guided 3 — Use boolean masks; Guided 4 — Standardize columns.
- Practical Lab: Analyze a matrix of student marks using NumPy only. Compute subject averages, student totals, pass status, and standardized scores.
**Practical tasks:**
- Create a 2-D array with at least five students and three subjects.
- Calculate subject means and standard deviations along the correct axis.
- Build a mask for students who passed every subject.
- Standardize columns and verify approximate zero mean.
**Extension:** Compare population standard deviation (`ddof=0`) with sample standard deviation (`ddof=1`). Add a missing value and use NaN-aware functions.
**Core references:** NumPy absolute beginners: https://numpy.org/doc/stable/user/absolute_beginners.html | NumPy reference: https://numpy.org/doc/stable/reference/

### Chapter 06 — Pandas I: Series, DataFrames, and Inspection
**Folder:** `Chapter_06_pandas_i_series_dataframes_and_inspection/`
**Purpose:** Pandas makes labelled, heterogeneous tabular data easier to inspect and manipulate. Focus on the data model, selection, indexing, dtypes, and descriptive summaries.
**Prerequisites:** Python and NumPy basics; install Pandas.
**Learning goals:**
- Explain Series, DataFrame, index, columns, and alignment.
- Read tabular data and inspect its structure.
- Select rows and columns with loc and iloc.
- Understand dtypes, missing values, and descriptive summaries.
**Section allocation and coverage:**
1. **Series and DataFrame** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. A `Series` is a one-dimensional labelled array with an index. A `DataFrame` is a two-dimensional labelled table whose columns may have different dtypes. Useful attributes: `.index`, `.columns`, `.dtypes`, `.shape`, `.ndim`, `.size`, `.empty`. Attributes do not use parentheses; methods such as `.head()` do. Keep column labels unique.…
2. **Reading tabular data** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `pd.read_csv(filepath_or_buffer, sep=",", header="infer", names=None, index_col=None, usecols=None, dtype=None, parse_dates=None, na_values=None, encoding=None)` reads delimited text. `usecols` reduces columns, `dtype` controls type inference, `parse_dates` converts date fields, `na_values` adds missing markers. Other readers include `read_json`, `read_excel`, `read_parquet`, and `read_sql`.…
3. **Selection and indexing** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `df["column"]` selects a Series; `df[["a","b"]]` selects multiple columns. `.loc[row_label, column_label]` is label-based; `.iloc[row_position, column_position]` is integer-position-based. `.loc` label slices include endpoint labels; `.iloc` follows Python-exclusive stop behavior. Use `.loc[mask, columns]` for explicit conditional selection and assignment.…
4. **Data types and index design** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Common dtypes: `int64`, `float64`, `bool`, `object`, `string`, `category`, and `datetime64`. Nullable extension dtypes (`Int64`, `boolean`, `string`) can represent missing values. An index labels rows but is not automatically a primary key. `set_index` and `reset_index` move values between columns and index; `astype` converts validated types; `to_datetime(errors="coerce")` turns invalid dates into `NaT`.…
5. **First-pass inspection** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `head(n=5)`, `tail(n=5)`, `info()`, `describe(include=..., exclude=...)`, `value_counts(dropna=True)`, `nunique(dropna=True)`, `isna`, and `notna` are core inspection methods. Numeric summaries do not prove data quality; separately validate ranges, allowed categories, uniqueness, dates, and foreign keys.…
**Notebook allocation:**
- Concepts and Theory: all section explanations plus concise demonstrations.
- Step-by-Step Tutorial: Guided 1 — Establish the shape; Guided 2 — Filter a region; Guided 3 — Summarize numeric columns; Guided 4 — Compute profit margin.
- Practical Lab: Perform an initial analysis of sales data. Establish the row grain, identify data types, select a regional subset, and compute a margin metric.
**Practical tasks:**
- Load sales.csv and inspect shape, info, and preview.
- Classify numeric, categorical, identifier, and date columns.
- Select North region orders with loc.
- Calculate row-level profit margin and total weighted margin.
**Extension:** Explain why a DataFrame row index is not a stable business key. Demonstrate after sorting and filtering.
**Core references:** Pandas getting started: https://pandas.pydata.org/docs/getting_started/index.html | Pandas user guide: https://pandas.pydata.org/docs/user_guide/index.html

### Chapter 07 — Pandas II: Cleaning, Transformation, and Aggregation
**Folder:** `Chapter_07_pandas_ii_cleaning_transformation_and_aggregation/`
**Purpose:** Real datasets are rarely analysis-ready. Learn missing-value handling, duplicate detection, strings, dates, grouping, joins, and reshaping.
**Prerequisites:** Chapter 6 DataFrame selection, dtypes, and inspection.
**Learning goals:**
- Diagnose missing values and duplicates.
- Use string, datetime, and categorical accessors.
- Transform with vectorized operations, map, and apply.
- Group, aggregate, merge, concatenate, pivot, and melt.
**Section allocation and coverage:**
1. **Missing values** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Pandas uses `np.nan`, `pd.NA`, and `NaT`. Use `isna`/`notna` for detection. `dropna(axis=0, how="any", subset=None, thresh=None)` removes rows/columns based on missingness. `fillna(value, limit=...)` accepts scalar, mapping, Series, or DataFrame values. Forward/backward filling is meaningful only when row order has temporal meaning. Decide whether missingness itself carries information.…
2. **Duplicates and strings** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `duplicated(subset=None, keep="first")` marks duplicate rows; `keep="last"` marks earlier copies; `keep=False` marks all members. `drop_duplicates(subset=None, keep="first", ignore_index=False)` removes duplicates. Define identity using business keys. The `.str` accessor includes `strip`, `lower`, `upper`, `replace`, `contains`, `startswith`, `len`, and `extract`; use `na=` where supported.…
3. **Dates and times** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `pd.to_datetime(arg, errors="raise", utc=False, format=None)` parses timestamps. `errors="coerce"` turns invalid values into `NaT`. `.dt` exposes year, month, day, quarter, and day name. `dt.to_period("M")` produces monthly periods; `dt.floor("D")` rounds down. Set a consistent timezone policy; UTC normalization may require local conversion for reporting.…
4. **GroupBy and aggregation** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `groupby(by, as_index=True, sort=True, dropna=True)` splits rows into groups. `.agg()` computes summaries; `.transform()` returns an aligned result; `.filter()` retains groups. Named aggregation such as `revenue_total=("revenue","sum")` gives stable names. Prefer built-in operations over Python `apply` where possible.…
5. **Merge and concat** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `pd.merge(left,right,how="inner",on=None,left_on=None,right_on=None,suffixes=("_x","_y"),validate=None,indicator=False)` joins relational keys. `inner`, `left`, `right`, and `outer` have different retention rules. `validate` can assert one-to-one, one-to-many, or many-to-one. `pd.concat(objs,axis=0,join="outer",ignore_index=False,keys=None)` stacks along rows or columns; use merge for keyed joins and concat for stack…
6. **Reshaping** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `pivot(index,columns,values)` requires unique key combinations. `pivot_table` aggregates duplicates and supports `aggfunc`, `fill_value`, and `margins`. `melt(id_vars,value_vars,var_name,value_name)` converts wide values to long form. Tidy/long data is convenient for plotting and statistical modeling.…
**Notebook allocation:**
- Concepts and Theory: all section explanations plus concise demonstrations.
- Step-by-Step Tutorial: Guided 1 — Preserve raw inputs; Guided 2 — Standardize and handle nulls; Guided 3 — Aggregate and rank; Guided 4 — Validate a customer join.
- Practical Lab: Clean a deliberately messy sales extract, create regional summaries, and join customer context without unintentionally multiplying rows.
**Practical tasks:**
- Measure missing values and duplicate order IDs before cleaning.
- Standardize product and region strings.
- Choose a documented missing-value rule.
- Aggregate revenue and profit by region.
- Join orders to customers and validate row count and match status.
**Extension:** Build a month-by-region pivot and a rolling three-month metric. Explain why sorting and missing-period policy are essential.
**Core references:** Missing data: https://pandas.pydata.org/docs/user_guide/missing_data.html | GroupBy guide: https://pandas.pydata.org/docs/user_guide/groupby.html | Merge guide: https://pandas.pydata.org/docs/user_guide/merging.html

### Chapter 08 — Polars and Apache Arrow for Efficient Data Processing
**Folder:** `Chapter_08_polars_and_apache_arrow_for_efficient_data_processing/`
**Purpose:** Polars offers an expression-based DataFrame API and lazy query optimization. Apache Arrow is a columnar memory format for efficient data interchange.
**Prerequisites:** Python, Pandas, SQL-style filtering/grouping; install `polars` and `pyarrow` for full examples.
**Learning goals:**
- Explain eager versus lazy execution and query plans.
- Use Polars expressions to select, filter, add, and aggregate columns.
- Read files lazily and collect results deliberately.
- Understand Arrow tables and interoperability.
**Section allocation and coverage:**
1. **Polars vs Pandas vs Arrow** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Pandas is a general-purpose DataFrame library. Polars emphasizes columnar execution, expressions, and parallel query processing. Apache Arrow is a language-independent columnar memory format and ecosystem, not a DataFrame API replacement. Polars is not a drop-in replacement for every Pandas workflow; choose based on workload and integrations.…
2. **Eager DataFrames and expression API** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `pl.DataFrame` constructs an eager frame. `select` returns selected/computed columns; `with_columns` adds or replaces; `filter` keeps rows; `group_by().agg()` aggregates; `sort` orders. Expressions: `pl.col`, `pl.lit`, `.cast`, `.alias`, `.sum`, `.mean`, `.is_null`, `.fill_null`, string expressions. Expressions describe work performed by a DataFrame operation.…
3. **Lazy execution** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `scan_csv(path)` creates a lazy source; `filter` and `select` build a plan. `collect()` executes/materializes; `explain()` displays the plan. Projection and predicate pushdown may avoid loading unnecessary columns/rows. Lazy mode is useful for multi-step pipelines; eager mode is convenient for small data. Benchmark on representative data.…
4. **Nulls, NaNs, and conversions** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Polars distinguishes null from floating-point NaN. Use `.is_null`/`.fill_null` for nulls and `.is_nan`/`.fill_nan` for NaN. Convert with `.to_pandas()` or `.to_arrow()` when required; conversion may add memory/time cost. PyArrow is required for some Arrow interoperability paths.…
**Notebook allocation:**
- Concepts and Theory: all section explanations plus concise demonstrations.
- Step-by-Step Tutorial: Guided 1 — Compare eager and lazy; Guided 2 — Filter and derive a column; Guided 3 — Aggregate lazily; Guided 4 — Inspect Arrow schema.
- Practical Lab: Reproduce a Pandas sales aggregation with Polars. Compare expression style and lazy execution.
**Practical tasks:**
- Read sales.csv with Polars.
- Create a derived profit column.
- Filter high-value orders.
- Aggregate revenue by region lazily.
- Convert to Arrow and inspect the schema.
**Extension:** Benchmark Polars lazy scanning against Pandas eager loading on a large generated CSV. Control for warm-up, input size, and memory. Explain why one benchmark cannot prove universal superiority.
**Core references:** Polars guide: https://docs.pola.rs/ | Apache Arrow: https://arrow.apache.org/docs/

### Chapter 09 — SQL Fundamentals and MySQL Connectivity
**Folder:** `Chapter_09_sql_fundamentals_and_mysql_connectivity/`
**Purpose:** SQL is the language for relational data. Connect relational design and query logic to Python database drivers, transactions, parameterized SQL, and safe resource handling.
**Prerequisites:** Basic tables and Python functions. MySQL server only needed for live-connection exercises; SQLite is used for local SQL drills.
**Learning goals:**
- Explain tables, rows, primary keys, and foreign keys.
- Write SELECT, WHERE, GROUP BY, HAVING, JOIN, and subqueries.
- Connect with mysql-connector-python or PyMySQL.
- Use parameterized statements, transactions, cursors, commits, and rollbacks.
**Section allocation and coverage:**
1. **Relational model and keys** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. A table contains rows at a defined grain. A primary key uniquely identifies a row; a foreign key references a key in another table. A one-to-many relationship stores the parent key on the many-side. Normalization limits update anomalies. Define the grain and key before designing joins.…
2. **SELECT query anatomy** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Typical SQL: `SELECT columns FROM table WHERE condition GROUP BY keys HAVING aggregate_condition ORDER BY expression LIMIT n`. Logical processing is conceptually FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT. `WHERE` filters rows; `HAVING` filters groups. `COUNT(*)` counts rows; `COUNT(column)` ignores NULL; `COUNT(DISTINCT column)` counts unique non-null values.…
3. **Joins and NULLs** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `INNER JOIN` keeps matching pairs; `LEFT JOIN` retains all left rows; `RIGHT JOIN` retains the right; `FULL OUTER JOIN` retains both where supported. Duplicate join keys can multiply rows. SQL uses three-valued logic: `column = NULL` is not a null test; use `IS NULL`/`IS NOT NULL`.…
4. **Python MySQL drivers** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `mysql.connector.connect(host, port=3306, user, password, database, connection_timeout=...)` opens Connector/Python connections. `connection.cursor()` yields a cursor; `execute`, `fetchone`, `fetchmany(size)`, and `fetchall` are DB-API patterns. `cursor(dictionary=True)` returns mappings with Connector/Python. PyMySQL is another DB-API driver; its cursor classes include `DictCursor`.…
5. **Parameters, transactions, and security** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Connector/Python and PyMySQL commonly use `%s` value placeholders; SQLite uses `?`. Pass values separately. Placeholders cannot safely stand for table or column identifiers; dynamic identifiers require allow-lists and proper quoting. `commit()` makes changes durable; `rollback()` cancels uncommitted work. Use try/except, close cursors/connections, environment variables, and least-privilege accounts.…
**Notebook allocation:**
- Concepts and Theory: all section explanations plus concise demonstrations.
- Step-by-Step Tutorial: Guided 1 — Read SQL rows; Guided 2 — Aggregate by group; Guided 3 — Use parameters; Guided 4 — Commit and rollback.
- Practical Lab: Practice SQL locally, then adapt the same query logic to a MySQL database using a real driver.
**Practical tasks:**
- Create customer and order tables with primary and foreign keys.
- Insert rows using parameterized statements.
- Write a JOIN grouped by city.
- Show how to rollback an update.
- Explain SQLite ? placeholders versus MySQL driver %s placeholders.
**Extension:** Implement an idempotent customer import using a unique business key. Compare MySQL `INSERT`, `INSERT IGNORE`, and `INSERT ... ON DUPLICATE KEY UPDATE` and test duplicate handling.
**Core references:** MySQL Reference: https://dev.mysql.com/doc/refman/8.4/en/ | Connector/Python: https://dev.mysql.com/doc/connector-python/en/ | PyMySQL: https://pymysql.readthedocs.io/

### Chapter 10 — SQLAlchemy and Pandas Database Workflows
**Folder:** `Chapter_10_sqlalchemy_and_pandas_database_workflows/`
**Purpose:** SQLAlchemy provides database connectivity and SQL expression/ORM layers. Pandas bridges SQL queries and DataFrames. Learn engines, connections, transactions, bind parameters, and table exchange.
**Prerequisites:** Chapter 9 SQL. Install SQLAlchemy; MySQL driver is optional for the SQLite demonstrations.
**Learning goals:**
- Distinguish Engine, Connection, Session, and ORM concepts.
- Create database URLs and configure connection behavior.
- Execute bound SQL with text().
- Read and write DataFrames to relational databases safely.
**Section allocation and coverage:**
1. **Engine, Connection, dialect, Session** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. An SQLAlchemy Engine is a long-lived factory and connection pool. A Connection is a checked-out DBAPI connection for statements. A Dialect adapts SQL to the database and driver. A Session is the ORM unit-of-work interface; simple analytical queries often need Core connections, not ORM objects. Reuse an engine rather than creating one for every query.…
2. **URLs and secrets** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. URL structure: `dialect+driver://username:password@host:port/database`. SQLite examples use `sqlite:///path.db` or `sqlite://` for memory. `URL.create()` avoids manual escaping of special characters. MySQL URLs can use `mysql+mysqlconnector://...` or `mysql+pymysql://...`. Build from environment variables or secret storage; do not hardcode credentials.…
3. **SQL text and parameters** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `text("SELECT ... WHERE key=:value")` creates a textual SQL expression with named bind parameters. Execute via `conn.execute(stmt,{"value":v})`. Use `engine.connect()` for queries; `engine.begin()` gives a transaction that commits on successful exit and rolls back on exception. SQLAlchemy 2.x favors explicit Connection execution.…
4. **Pandas SQL integration** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `pd.read_sql(sql, con, params=None, parse_dates=None, ...)` reads a query/table into a DataFrame. `DataFrame.to_sql(name, con, if_exists="fail", index=True, chunksize=None, dtype=None, method=None)` writes. `if_exists` options: fail, replace, append. `replace` drops/recreates a table and can destroy constraints/indexes. `index=False` prevents an unwanted index column.…
5. **Pools and performance** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Engine pool arguments include `pool_size`, `max_overflow`, `pool_timeout`, and `pool_recycle`; tune based on workload, not guesses. `chunksize` batches inserts; `method="multi"` can improve inserts where the driver supports it. For very large imports, use database-native bulk loading. Validate row counts and constraints after loads.…
**Notebook allocation:**
- Concepts and Theory: all section explanations plus concise demonstrations.
- Step-by-Step Tutorial: Guided 1 — Use transactions; Guided 2 — Read with Pandas; Guided 3 — Append a frame; Guided 4 — Configure MySQL.
- Practical Lab: Build a local SQLAlchemy/Pandas workflow, query results into a DataFrame, append a frame, then document how to enable the same approach with MySQL.
**Practical tasks:**
- Create a local SQLite engine.
- Create and populate a table with bound parameters.
- Read results into Pandas.
- Append rows with to_sql.
- Explain the risks of replace and the role of transactions.
**Extension:** Add a staging table, validation queries, and an explicit transaction. Compare Core connections with ORM sessions for analytical extraction.
**Core references:** SQLAlchemy 2.0 Tutorial: https://docs.sqlalchemy.org/en/20/tutorial/ | Engine configuration: https://docs.sqlalchemy.org/en/20/core/engines.html | Pandas SQL IO: https://pandas.pydata.org/docs/user_guide/io.html#sql-queries

### Chapter 11 — Matplotlib: Foundational Data Visualization
**Folder:** `Chapter_11_matplotlib_foundational_data_visualization/`
**Purpose:** Matplotlib is the core plotting library. Learn figures, axes, plot types, labels, scales, legends, layout, and export controls.
**Prerequisites:** NumPy/Pandas basics; install Matplotlib.
**Learning goals:**
- Distinguish Figure and Axes objects.
- Create line, bar, scatter, histogram, and box plots.
- Control labels, scales, legends, grids, and layouts.
- Export charts with readable dimensions and resolution.
**Section allocation and coverage:**
1. **Figure and Axes** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. A Figure is the overall canvas; an Axes is one plotting area. Prefer `fig, ax = plt.subplots(...)`, then `ax.plot`, `ax.set_title`, and `ax.legend`. Stateful `plt` functions are quick shortcuts; the object-oriented API is easier for multi-panel charts and reusable functions.…
2. **Figure construction** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `plt.subplots(nrows=1,ncols=1,figsize=None,sharex=False,sharey=False,squeeze=True,layout=None)` returns a Figure and Axes. `figsize` uses inches; `sharex/sharey` synchronize axes; `squeeze=False` guarantees a 2-D axes array; `layout="constrained"` helps prevent clipping. Save via `fig.savefig(fname,dpi=...,bbox_inches="tight")`; close figures in loops.…
3. **Chart methods** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `ax.plot(x,y,marker,linestyle,linewidth,label)` shows trends; `bar`/`barh` compares categories; `scatter(x,y,s,c,alpha)` shows relationships; `hist(x,bins,density,cumulative)` shows distributions; `boxplot` shows quartiles and potential outliers. Select chart type based on variable types and the analytical question.…
4. **Axes and annotations** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Use `set_title`, `set_xlabel`, `set_ylabel`, `set_xlim`, `set_ylim`, `set_xscale`, `set_yscale`, `grid`, and `legend`. Log scales change visual interpretation; label them. Avoid misleading truncated axes and make units, periods, and denominator clear.…
5. **Export and accessibility** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `dpi` controls raster resolution; SVG/PDF are vector formats. Keep labels readable at the final size, check contrast, and do not encode critical meaning by color alone. Save the final figure after setting labels and layout.…
**Notebook allocation:**
- Concepts and Theory: all section explanations plus concise demonstrations.
- Step-by-Step Tutorial: Guided 1 — Compare regional revenue; Guided 2 — Examine a time trend; Guided 3 — Inspect profit distribution; Guided 4 — Export the final chart.
- Practical Lab: Create a sales visual report with regional revenue, daily revenue, and profit distribution. Every chart must have a title, axes, units, and readable layout.
**Practical tasks:**
- Aggregate regional revenue.
- Parse dates and plot daily revenue chronologically.
- Plot the distribution of profit.
- Save one chart as PNG and SVG.
**Extension:** Create a 2x2 dashboard with KPIs and a rolling average over daily revenue. Explain how window size changes the interpretation.
**Core references:** Matplotlib quick start: https://matplotlib.org/stable/users/explain/quick_start.html | Pyplot API: https://matplotlib.org/stable/api/pyplot_summary.html

### Chapter 12 — Seaborn: Statistical Data Visualization
**Folder:** `Chapter_12_seaborn_statistical_data_visualization/`
**Purpose:** Seaborn builds statistical graphics on Matplotlib with high-level functions, semantic mappings, statistical estimators, and attractive defaults.
**Prerequisites:** Pandas DataFrames and basic Matplotlib; install Seaborn.
**Learning goals:**
- Understand long-form and wide-form data.
- Use axes-level and figure-level plotting functions.
- Create distribution, relational, categorical, and matrix plots.
- Interpret hue, facets, estimators, and confidence intervals.
**Section allocation and coverage:**
1. **Data model and semantics** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Seaborn supports long and wide data; long form is usually clearer. Map with `data`, `x`, `y`, `hue`, `style`, and `size`. `hue` encodes categorical color, `style` marker/line type, and `size` a quantitative channel. Axes-level functions draw on a Matplotlib Axes (`scatterplot`, `histplot`, `boxplot`); figure-level functions manage grids (`relplot`, `displot`, `catplot`, `pairplot`).…
2. **Relational plots** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `scatterplot(data,x,y,hue,style,size,alpha,...)` maps pairs. `lineplot` aggregates repeated observations by default and may show uncertainty; set `estimator=None` for raw lines. Confidence intervals around an estimate express uncertainty in an estimated statistic, not the range of individual values.…
3. **Distribution plots** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `histplot(data,x,bins="auto",stat="count",kde=False,...)` displays binned values. `kdeplot` estimates smooth density; bandwidth affects shape. `ecdfplot` shows the empirical cumulative distribution. `stat="density"` normalizes area rather than counts. Use consistent bins/scales for comparisons.…
4. **Categorical plots** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `barplot` estimates a statistic (mean by default); `countplot` counts observations. `boxplot` shows quartiles and whisker rules (`whis`); `violinplot` adds density; `stripplot`/`swarmplot` show observations. A mean bar is not a raw count. Consider median and spread where distributions are skewed.…
5. **Heatmaps, pair plots, facets** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `heatmap(data,annot,fmt,cmap,center,vmin,vmax)` maps matrix values to color. Correlation heatmaps show linear association, not causation. `pairplot(data,hue,vars,diag_kind)` can be expensive with many columns. Figure-level plots support row/column facets for small multiples.…
**Notebook allocation:**
- Concepts and Theory: all section explanations plus concise demonstrations.
- Step-by-Step Tutorial: Guided 1 — Compare distributions; Guided 2 — Examine numeric association; Guided 3 — Compare group means and spread; Guided 4 — Check correlation.
- Practical Lab: Create a statistical visual report using distributions, relationships, categorical comparisons, and correlation. Explain what each chart can and cannot establish.
**Practical tasks:**
- Plot revenue distributions by region with comparable bins.
- Examine units versus revenue grouped by product.
- Compare mean profit by region and explain the estimator.
- Create a correlation heatmap and state one caveat.
**Extension:** Use `relplot` or `catplot` for small multiples. Compare median with mean profit and explain what changes.
**Core references:** Seaborn tutorial: https://seaborn.pydata.org/tutorial.html | Seaborn API: https://seaborn.pydata.org/api.html

### Chapter 13 — Interactive Visualization with Plotly, Bokeh, and Altair
**Folder:** `Chapter_13_interactive_visualization_with_plotly_bokeh_and_altair/`
**Purpose:** Interactive charts support hover, zoom, selection, and linked views. Compare three libraries and their interaction models.
**Prerequisites:** Pandas, Matplotlib concepts, and chart grammar; full stack includes Plotly, Bokeh, and Altair.
**Learning goals:**
- Build Plotly Express and Graph Objects charts.
- Understand Bokeh figures, glyphs, sources, and tools.
- Create declarative Altair charts and encodings.
- Choose a library based on interaction, deployment, performance, and fit.
**Section allocation and coverage:**
1. **Plotly Express and Graph Objects** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Plotly Express (`px`) is a high-level API: `px.scatter(data_frame,x,y,color,size,hover_name,facet_col,...)`; other functions include `line`, `bar`, `histogram`, and `box`. Graph Objects (`go`) gives lower-level control with `go.Figure`, traces (`go.Scatter`, `go.Bar`), `update_layout`, and `update_traces`. Use Express for common charts and Graph Objects for trace-level control.…
2. **Layout and interaction** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. A Plotly Figure has `data` traces and a `layout`. Use `update_layout(title,xaxis_title,yaxis_title,template)` and `update_traces(hovertemplate=...)`. `fig.show()` renders; `write_html(path,include_plotlyjs=...)` exports HTML. Give the default chart a useful view and hover fields; excessive interaction can add friction.…
3. **Bokeh model** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `figure()` creates a plot. Glyphs such as `line`, `circle`, `scatter`, and `vbar` add marks. `ColumnDataSource` provides named columns for linked selection and hover tools. Tools include pan, wheel zoom, box zoom, reset, save, and hover. Use `output_file`/`save` for HTML output or notebook output for inline rendering.…
4. **Altair and chart grammar** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Altair is declarative: `alt.Chart(data).mark_point().encode(x="units:Q",y="revenue:Q",color="region:N")`. Types: `Q` quantitative, `N` nominal, `O` ordinal, `T` temporal. Transforms include `transform_filter`, `transform_aggregate`, and `transform_calculate`. Parameters/selections drive interactive filters. Large datasets may encounter row limits.…
5. **Library selection** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Plotly has broad chart coverage and integrates with dashboard frameworks; Bokeh offers browser-oriented plot models and linked interactions; Altair provides concise declarative specifications. Evaluate deployment, accessibility, performance, maintainability, team skill, and offline behavior.…
**Notebook allocation:**
- Concepts and Theory: all section explanations plus concise demonstrations.
- Step-by-Step Tutorial: Guided 1 — Create a Plotly figure; Guided 2 — Customize a trace; Guided 3 — Add a Bokeh bar glyph; Guided 4 — Declare a chart with Altair.
- Practical Lab: Build an interactive regional sales exploration using multiple libraries, then compare their syntax and interaction models.
**Practical tasks:**
- Create a Plotly revenue bar chart with hover values.
- Create Graph Objects product-profit chart.
- Build Bokeh glyph visualization if installed.
- Build Altair scatter chart if installed.
- Select a library for a dashboard and justify the choice.
**Extension:** Add date-range filters and a linked selection. Export to HTML and verify the chart in a browser without a running notebook server.
**Core references:** Plotly: https://plotly.com/python/ | Bokeh: https://docs.bokeh.org/en/latest/docs/user_guide.html | Altair: https://altair-viz.github.io/

### Chapter 14 — Scientific Statistics with SciPy
**Folder:** `Chapter_14_scientific_statistics_with_scipy/`
**Purpose:** SciPy adds established numerical algorithms and statistical procedures on top of NumPy. This chapter focuses on distributions, descriptive statistics, confidence intervals, hypothesis tests, correlation, and interpretation.
**Prerequisites:** NumPy arrays, Pandas filtering/grouping, and foundational probability concepts.
**Learning goals:**
- Select and parameterize continuous and discrete probability distributions.
- Compute descriptive statistics and confidence intervals.
- Choose and interpret common hypothesis tests.
- Assess correlation and avoid common inferential errors.
**Section allocation and coverage:**
1. **SciPy architecture and stats module** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. SciPy is a collection of scientific-computing subpackages. `scipy.stats` provides distributions, summary statistics, tests, and correlation measures. A frozen distribution object stores parameters and exposes methods such as `pdf`, `pmf`, `cdf`, `ppf`, `rvs`, `mean`, and `var`. The `loc` and `scale` parameters shift and scale many continuous distributions; distribution-specific shape parameters define form.…
2. **Descriptive statistics** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `stats.describe(a, axis=0, ddof=1, bias=True, nan_policy="propagate")` reports count, minimum/maximum, mean, variance, skewness, and kurtosis. `stats.iqr(a, axis=None, rng=(25,75), scale=1.0, nan_policy=...)` measures a quantile range. `stats.trim_mean(a, proportiontocut, axis=0)` removes equal tail proportions before averaging. Know whether a function uses sample or population variance and whether kurtosis is Fisher…
3. **Probability distributions** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Examples: `stats.norm(loc,scale)`, `stats.t(df,loc,scale)`, `stats.binom(n,p)`, `stats.poisson(mu)`, and `stats.expon(scale)`. `pdf` is a density, not point probability; `pmf` is a discrete point probability. `cdf(x)` gives cumulative probability; `sf(x)` is often more numerically stable for upper tails; `ppf(q)` is the quantile function. `rvs(size, random_state)` draws random samples.…
4. **Hypothesis testing** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. A test returns a statistic and p-value. A p-value is the probability, under the null and test assumptions, of data at least as extreme as observed; it is not the probability that the null is true. `ttest_1samp`, `ttest_ind`, and `ttest_rel` address one-sample, independent-group, and paired mean comparisons. `equal_var=False` in `ttest_ind` gives Welch’s test. Check independence, sampling design, distributional assump…
5. **Proportions, association, and multiple testing** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `chi2_contingency` tests independence in a contingency table; `fisher_exact` is useful for small 2x2 tables. `pearsonr` measures linear association and provides a test; `spearmanr` uses ranks and captures monotonic association. Multiple comparisons increase false-positive risk; adjust p-values or pre-specify comparisons. Statistical significance is distinct from practical importance and causal evidence.…
6. **Confidence intervals and effect sizes** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. A confidence interval is generated by a procedure with a stated long-run coverage level under assumptions. For a mean with unknown standard deviation, a t interval uses sample standard error and a t critical value. Report effect size, interval, sample size, and test assumptions rather than only a p-value.…
**Notebook allocation:**
- Concepts and Theory: all section explanations plus concise demonstrations.
- Step-by-Step Tutorial: Guided 1 — Describe before testing; Guided 2 — Match a test to the design; Guided 3 — Interpret probability and p-values; Guided 4 — Report an interval.
- Practical Lab: Analyze whether order-level profit differs across regions. Your report must separate descriptive patterns, inferential evidence, effect magnitude, and limitations.
**Practical tasks:**
- Summarize profit by region with sample size, mean, median, and standard deviation.
- Choose a justified two-group comparison and use Welch’s t-test.
- Calculate a confidence interval for one regional mean.
- Examine Pearson and Spearman correlations for units and revenue.
- Write an interpretation that avoids causal claims and explains the p-value.
**Extension:** Use a permutation test or bootstrap to estimate uncertainty in the difference of means. Discuss what changes if you compare all six region pairs and how multiplicity should be handled.
**Core references:** SciPy statistics: https://docs.scipy.org/doc/scipy/reference/stats.html | SciPy hypothesis tests: https://docs.scipy.org/doc/scipy/reference/stats.html#hypothesis-tests

### Chapter 15 — Statistical Modeling with Statsmodels
**Folder:** `Chapter_15_statistical_modeling_with_statsmodels/`
**Purpose:** Statsmodels provides interpretable statistical models with coefficient estimates, uncertainty measures, diagnostics, and formal inference. Learn linear regression, categorical predictors, residual analysis, and time-series foundations.
**Prerequisites:** Pandas, NumPy, descriptive statistics, and basic probability; SciPy statistics is recommended.
**Learning goals:**
- Fit and interpret ordinary least squares regression.
- Use formulas and categorical variables safely.
- Interpret coefficients, confidence intervals, p-values, and model fit.
- Evaluate residual assumptions and recognize model limitations.
- Understand the introductory workflow for time-series analysis.
**Section allocation and coverage:**
1. **Model specification and design matrices** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `statsmodels.api.OLS(endog, exog, missing="none")` fits a linear model; add an intercept explicitly with `sm.add_constant(X)`. Formula API `statsmodels.formula.api.ols("y ~ x1 + C(group)", data=df)` creates design matrices and handles categorical terms via `C()`. Formula operators include `+`, `:`, `*` (main effects plus interaction), and `-1` (remove intercept).…
2. **Fit and inspect an OLS model** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `model.fit(cov_type="nonrobust")` estimates coefficients; common robust covariance options include `HC0`–`HC3`, which alter standard errors and inference, not fitted coefficients. `summary()` provides coefficient table, confidence intervals, R-squared, F-statistic, and diagnostics. A coefficient is conditional on the other included predictors and model specification.…
3. **Inference and model fit** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `params`, `bse`, `tvalues`, `pvalues`, `conf_int()`, `rsquared`, `rsquared_adj`, `fittedvalues`, and `resid` expose key results. R-squared is the fraction of outcome variation explained in-sample under the model definition; it does not establish causation, correct specification, or out-of-sample performance.…
4. **Assumptions and diagnostics** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Classical OLS inference relies on a suitable linear conditional mean, independent errors, and assumptions for standard errors (homoscedasticity for conventional covariance; normality for exact small-sample t/F inference). Inspect residual-versus-fitted plots, Q-Q plots, leverage, influence, multicollinearity, and time ordering. Heteroscedasticity-robust standard errors do not fix omitted-variable bias or nonlinear sp…
5. **Prediction and leakage** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Separate training and test periods or samples when evaluating prediction. Confidence intervals for the mean response are narrower than prediction intervals for a new observation. Never use future information in predictors for a historical prediction task. Do not interpret observational regression coefficients as causal effects without a defensible identification strategy.…
6. **Time-series entry points** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Time series observations are ordered and often autocorrelated. Statsmodels includes ACF/PACF tools, ARIMA/SARIMAX, exponential smoothing, and decomposition. Split chronologically, inspect trend/seasonality, and avoid random train/test splits for forecasting. Check residual autocorrelation and compare against simple baselines.…
**Notebook allocation:**
- Concepts and Theory: all section explanations plus concise demonstrations.
- Step-by-Step Tutorial: Guided 1 — Define the model question; Guided 2 — Fit and read the coefficient table; Guided 3 — Diagnose residual structure; Guided 4 — Compare conventional and robust inference.
- Practical Lab: Build an interpretable model of revenue using units, discount, and region. Explain the reference category, coefficient units, model fit, residual diagnostics, and limits of causal interpretation.
**Practical tasks:**
- Fit `revenue ~ units + discount + C(region)`.
- Interpret the units and discount coefficients with units and caveats.
- Compare conventional and HC3 standard errors.
- Make a residual-versus-fitted plot and a Q-Q plot.
- Evaluate out-of-sample prediction separately from in-sample fit.
**Extension:** Add a units-by-discount interaction and compare it with the main-effects model using an appropriate nested model comparison. Check collinearity and explain why model fit alone cannot establish causality.
**Core references:** Statsmodels user guide: https://www.statsmodels.org/stable/user-guide.html | Formula examples: https://www.statsmodels.org/stable/examples/index.html

### Chapter 16 — Exploratory Data Analysis and Data Quality
**Folder:** `Chapter_16_exploratory_data_analysis_and_data_quality/`
**Purpose:** Exploratory data analysis (EDA) combines data contracts, missingness analysis, outlier investigation, distributions, relationships, and communication. It turns a raw dataset into a defensible analytical starting point.
**Prerequisites:** Pandas, NumPy, basic plotting, and introductory statistics.
**Learning goals:**
- Define grain, keys, and quality rules before analyzing.
- Profile missingness, duplicates, types, ranges, and categories.
- Investigate outliers without blindly deleting them.
- Explore univariate and multivariate structure.
- Create a reproducible EDA summary and communicate caveats.
**Section allocation and coverage:**
1. **Data grain and data contracts** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Grain states what one row represents (for example, one order line or one customer). Define primary keys, candidate keys, required fields, allowed categories, units, date ranges, and relationships. A duplicate row may be an error or a valid repeated event; uniqueness must be defined at the correct grain. Validate assumptions explicitly with assertions or schema libraries.…
2. **Missingness** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `isna()` identifies missing values; `notna()` identifies present values; `isna().mean()` gives missing proportion. Missing completely at random, missing at random, and missing not at random are conceptual mechanisms, not conclusions available from a missingness heatmap alone. Distinguish not applicable, not collected, unknown, and true zero. Imputation can create bias if its assumptions are wrong.…
3. **Duplicates, types, and ranges** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Use `duplicated(subset=..., keep=...)`, `drop_duplicates`, `to_datetime(errors="coerce")`, `to_numeric(errors="coerce")`, and `.astype(...)`. Validate ranges and category domains. Coercion converts invalid strings to missing; count and review these conversions rather than silently accepting them.…
4. **Outliers and robust summaries** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Outliers may indicate data errors, rare valid events, or a different population. Investigate source records and units. IQR fences are exploratory flags, not universal deletion rules. Compare mean with median and standard deviation with IQR/MAD. Winsorization and trimming change the estimand and should be justified and documented.…
5. **Automated profiling** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. YData Profiling can create a rich HTML report with types, distributions, correlations, missingness, and warnings. The report is a discovery aid, not a substitute for domain review. Large datasets can generate slow or overly verbose reports; sample carefully and preserve privacy.…
6. **Communicating an EDA** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. A useful handoff states the dataset source, time period, grain, row/column count, key quality findings, transformations, metrics, notable patterns, limitations, and next questions. Separate findings from hypotheses and label exploratory patterns as such.…
**Notebook allocation:**
- Concepts and Theory: all section explanations plus concise demonstrations.
- Step-by-Step Tutorial: Guided 1 — State the grain and key; Guided 2 — Quantify missingness; Guided 3 — Clean text and numeric fields; Guided 4 — Review rather than auto-delete outliers.
- Practical Lab: Produce a reproducible EDA and data-quality report for the intentionally messy sales dataset. Do not silently discard records or impute values without justification.
**Practical tasks:**
- Describe the data grain and expected key.
- Report missingness and duplicate counts.
- Parse dates and numeric fields and count coercion failures.
- Normalize text columns while retaining a raw copy.
- Flag IQR outliers and inspect source rows.
- Summarize at least three findings and three limitations.
**Extension:** Create a data validation function that checks required columns, key uniqueness, accepted category values, numeric ranges, and date parse success. Return a structured list of errors and warnings rather than stopping at the first issue.
**Core references:** Pandas missing data: https://pandas.pydata.org/docs/user_guide/missing_data.html | YData Profiling: https://docs.profiling.ydata.ai/

### Chapter 17 — Machine Learning with Scikit-learn
**Folder:** `Chapter_17_machine_learning_with_scikit_learn/`
**Purpose:** Scikit-learn provides a consistent API for preprocessing, model fitting, evaluation, and model selection. Learn the end-to-end supervised-learning workflow while avoiding leakage and overclaiming.
**Prerequisites:** Python, NumPy, Pandas, descriptive statistics, and basic train/test reasoning.
**Learning goals:**
- Define features, target, task type, and a baseline.
- Split data before fitting transformations.
- Build preprocessing and estimator pipelines.
- Train regression and classification models.
- Evaluate with task-appropriate metrics and cross-validation.
- Recognize leakage, overfitting, and reproducibility requirements.
**Section allocation and coverage:**
1. **Estimator API** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Most estimators follow `fit(X, y)`, `predict(X)`, and sometimes `predict_proba(X)`. Transformers expose `fit`, `transform`, and `fit_transform`. `get_params()` inspects hyperparameters; `set_params()` changes them. Inputs are commonly arrays or DataFrames with rows as samples and columns as features; preserve feature names where possible.…
2. **Splitting and leakage** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `train_test_split(X,y,test_size,train_size,random_state,shuffle,stratify)` separates data. Split before fitting imputation, scaling, feature selection, or encoders. Leakage occurs when information unavailable at prediction time enters training, including preprocessing fitted on all rows and future time information. For grouped or temporal data use group/time-aware splitters, not random splitting.…
3. **Preprocessing and pipelines** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `SimpleImputer(strategy=...)` fills missing values; `StandardScaler` centers/scales; `OneHotEncoder(handle_unknown="ignore")` encodes categories. `ColumnTransformer` applies transformations to subsets of columns. `Pipeline(steps=[...])` chains steps and fits them inside each validation fold, reducing leakage risk. Sparse/dense output depends on encoder configuration and data.…
4. **Regression and classification** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Regression targets are numeric; common baselines include `DummyRegressor`, `LinearRegression`, and tree-based regressors. Classification predicts classes; models include `LogisticRegression`, decision trees, random forests, and support vector machines. Classification probabilities require calibration checks before high-stakes threshold decisions.…
5. **Evaluation metrics** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Regression: MAE, MSE/RMSE, and R-squared; interpret units and outlier sensitivity. Classification: confusion matrix, accuracy, precision, recall, F1, ROC-AUC, and PR-AUC. Metrics depend on class balance and decision thresholds. Always compare with a baseline and report the data split and evaluation sample.…
6. **Cross-validation and tuning** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `cross_val_score` estimates performance across folds. `GridSearchCV` and `RandomizedSearchCV` tune parameters; their search must be conducted within training data, leaving a final test set untouched. `scoring` determines the metric; `cv` determines fold strategy. Set random seeds where applicable and record versions.…
**Notebook allocation:**
- Concepts and Theory: all section explanations plus concise demonstrations.
- Step-by-Step Tutorial: Guided 1 — Define target and baseline; Guided 2 — Fit and evaluate a linear model; Guided 3 — Compare with cross-validation; Guided 4 — Inspect residuals.
- Practical Lab: Build a leakage-aware regression workflow for order revenue and a separate classification workflow using a built-in Scikit-learn dataset. Report baselines, preprocessing, metrics, and limitations.
**Practical tasks:**
- Define feature columns and target.
- Create a reproducible train/test split.
- Fit a DummyRegressor baseline and a LinearRegression model.
- Build a mixed numeric/categorical Pipeline with ColumnTransformer.
- Evaluate using MAE, RMSE, and R-squared.
- Run cross-validation and tune a model using training data only.
- Explain at least two possible leakage paths.
**Extension:** Use a time-aware split with order_date, create features that would genuinely be known at prediction time, compare a tree ensemble with a linear baseline, and explain how an apparently strong feature could leak the target.
**Core references:** Scikit-learn user guide: https://scikit-learn.org/stable/user_guide.html | Common pitfalls and leakage: https://scikit-learn.org/stable/common_pitfalls.html

### Chapter 18 — Building Data Applications with Streamlit
**Folder:** `Chapter_18_building_data_applications_with_streamlit/`
**Purpose:** Streamlit turns Python scripts into interactive data applications. Learn the execution model, input widgets, caching, charts, data loading, secrets, and deployment considerations.
**Prerequisites:** Python, Pandas, and at least one visualization library; install Streamlit separately.
**Learning goals:**
- Explain Streamlit’s script rerun model.
- Build layouts with titles, columns, containers, and sidebar widgets.
- Use caching appropriately for data and resources.
- Connect CSV and MySQL data safely.
- Structure, test, and deploy a small analytical application.
**Section allocation and coverage:**
1. **Execution model and display API** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. A Streamlit app is a Python script run by `streamlit run app.py`. Widget interactions trigger a script rerun from top to bottom. Display functions include `st.title`, `header`, `subheader`, `write`, `markdown`, `dataframe`, `table`, `metric`, and chart methods such as `line_chart` and `plotly_chart`. Use a clear top-to-bottom flow and avoid expensive unguarded work on every rerun.…
2. **Layout and widgets** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `st.sidebar`, `st.columns`, `st.container`, `st.expander`, and `st.tabs` organize content. Widgets include `selectbox`, `multiselect`, `slider`, `date_input`, `text_input`, `number_input`, `checkbox`, `radio`, `file_uploader`, and `button`. Most return the current selection/value; `key` gives a stable identity. Widget state is managed by Streamlit and can be explicitly read through `st.session_state`.…
3. **Caching and session state** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. `@st.cache_data` caches serializable data results and returns copies; `@st.cache_resource` caches shared resources such as database connections or ML models. Configure TTL, max entries, and hash behavior deliberately. `st.session_state` persists values across reruns for a user session. Caching must not expose one user’s private data to another; include user/security context in cache keys where relevant.…
4. **Data sources and secrets** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Use Pandas readers for uploaded CSV/Excel files. Database credentials belong in Streamlit secrets (`.streamlit/secrets.toml`) or environment variables, never committed source files. Use parameterized SQL, read-only credentials for dashboards, connection timeouts, and explicit error handling. Treat uploaded files as untrusted input and validate size, schema, and content.…
5. **Application architecture and deployment** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Separate loading, cleaning, metric calculation, and display functions. Use stable schemas and cache expensive read-only queries with a suitable TTL. Test filtering edge cases, missing data, empty results, and large inputs. Deploy with pinned dependencies, secrets management, resource limits, and a refresh strategy. The app script itself is the application; notebook cells are a learning environment.…
**Notebook allocation:**
- Concepts and Theory: all section explanations plus concise demonstrations.
- Step-by-Step Tutorial: Guided 1 — Define the app layout; Guided 2 — Add user controls; Guided 3 — Add KPIs and charts; Guided 4 — Run and test.
- Practical Lab: Build a regional sales dashboard with filters, KPIs, a trend chart, a detail table, and an optional MySQL source. Separate reusable logic from UI components.
**Practical tasks:**
- Create a Streamlit script with page configuration and title.
- Load sales.csv using a cached function.
- Add region and product filters.
- Display order count, revenue, and profit KPIs.
- Plot revenue over time and by region.
- Add a data table and CSV download.
- Document how to configure database secrets without committing credentials.
**Extension:** Add date filters, a Plotly chart, data-quality warnings, pagination or row limits, and a MySQL backend using secrets/environment variables. Test access control and cache isolation.
**Core references:** Streamlit documentation: https://docs.streamlit.io/ | Caching: https://docs.streamlit.io/develop/concepts/architecture/caching

### Chapter 19 — End-to-End Data Analysis Capstone
**Folder:** `Chapter_19_end_to_end_data_analysis_capstone/`
**Purpose:** Combine file ingestion, validation, SQL, Pandas, statistics, visualization, machine learning, and communication into a reproducible portfolio project. Use the supplied synthetic sales/customer datasets.
**Prerequisites:** Completion of the earlier foundations, processing, database, visualization, and analysis chapters.
**Learning goals:**
- Design a complete analytical workflow from a business question.
- Load, validate, clean, and join multiple data sources.
- Create reproducible metrics and statistical analyses.
- Build visual findings and a simple predictive baseline.
- Deliver a documented notebook, exported outputs, and dashboard-ready dataset.
**Section allocation and coverage:**
1. **Project brief and analytical questions** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. The fictional business wants to understand revenue and profit patterns by region, product, customer segment, and time. Define decisions the analysis could inform, not just charts to produce. Establish the unit of analysis, metric definitions, reporting period, and exclusions before computing results.…
2. **Data integration and validation** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Load order-level sales, customer reference data, and optional JSON metadata. Check key uniqueness, referential integrity, valid dates, non-negative units, financial arithmetic, and missingness. Join on explicit keys and verify expected row counts after each join. Avoid many-to-many joins unless that relationship is intended.…
3. **Metric design** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Define revenue, gross profit, profit margin, order count, units sold, average order value, and customer counts. Distinguish sum of row-level margin from ratio of totals. Define time granularity, currency, handling of refunds, and denominator for each rate. Store metric calculations in reusable functions.…
4. **Statistical reasoning** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Use descriptive summaries and uncertainty intervals to distinguish large samples from stable patterns. Explore relationships, inspect group distributions, and test pre-specified comparisons. Avoid multiple unplanned tests and causal claims from observational records. Include practical effect magnitude and uncertainty.…
5. **Visualization and narrative** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. Build a compact executive view, detailed diagnostic charts, and a data-quality section. Label axes with units, use appropriate aggregation, avoid misleading truncated scales, and annotate sample sizes. Write a headline, evidence, caveat, and action implication for each finding.…
6. **Reproducibility and handoff** — approximately 2–4 notebook screens of theory, terminology, parameter semantics, examples, and limitations. The final project should run from a clean environment, use relative paths, declare dependencies, avoid secrets, and preserve raw source files. Export a cleaned dataset, summary tables, charts, and a concise report. Include a README explaining data provenance, definitions, run order, limitations, and next steps.…
**Notebook allocation:**
- Concepts and Theory: all section explanations plus concise demonstrations.
- Step-by-Step Tutorial: Load and validate the project datasets; Join customer attributes; Create business metrics; Create a time-series summary; Visualize and export results; Optional SQL aggregation with SQLite.
- Practical Lab: Prepare an analyst-ready sales performance report for management. Use the included orders and customer datasets, with transparent metrics, reproducible data-quality checks, and visual evidence.
**Practical tasks:**
- Write three business questions and define metrics before analysis.
- Load orders and customers; validate primary and foreign keys.
- Perform a validated many-to-one merge.
- Compute revenue, profit, margin, AOV, orders, and units.
- Compare product, region, and customer segment.
- Create daily and monthly trends, plus a 7-day rolling metric.
- Conduct one inferential analysis with assumptions and uncertainty.
- Build a baseline predictive model without leakage.
- Create an executive summary with three evidence-backed findings and limitations.
- Export cleaned data, metric tables, and at least two charts.
**Extension:** Extend the project with a monthly cohort view, customer retention definition, forecast baseline, model monitoring plan, automated quality tests, and a Streamlit application. State which conclusions are descriptive, predictive, or causal—and justify each label.
**Core references:** Pandas merge: https://pandas.pydata.org/docs/user_guide/merging.html | Scikit-learn model evaluation: https://scikit-learn.org/stable/modules/model_evaluation.html | Streamlit docs: https://docs.streamlit.io/

## Cross-book projects
The capstone uses a consistent synthetic retail dataset: orders, customers, and JSON examples. The same concepts are revisited through file ingestion, database queries, transformation, statistical reasoning, visualization, machine learning, and dashboards.

## Prerequisite and environment notes
- Python 3.10 or later is recommended.
- Core lessons use widely available packages. Optional libraries are marked in notebooks and guarded where possible.
- A MySQL server is not bundled. MySQL chapters provide a local SQLite fallback for runnable SQL demonstrations and a MySQL connection pattern for a separately configured server.
- Streamlit apps run as scripts with `streamlit run app.py`; notebook cells explain and generate the app source.
- Network/API examples use a local saved response for offline execution; live calls are optional and should respect API terms and rate limits.