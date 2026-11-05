# Chapter 08 — Polars and Apache Arrow for Efficient Data Processing

**Purpose:** Polars offers an expression-based DataFrame API and lazy query optimization. Apache Arrow is a columnar memory format for efficient data interchange.

**Prerequisites:** Python, Pandas, SQL-style filtering/grouping; install `polars` and `pyarrow` for full examples.

## Learning goals
- Explain eager versus lazy execution and query plans.
- Use Polars expressions to select, filter, add, and aggregate columns.
- Read files lazily and collect results deliberately.
- Understand Arrow tables and interoperability.

## Topic and subtopic plan
### 1. Polars vs Pandas vs Arrow
Pandas is a general-purpose DataFrame library. Polars emphasizes columnar execution, expressions, and parallel query processing. Apache Arrow is a language-independent columnar memory format and ecosystem, not a DataFrame API replacement. Polars is not a drop-in replacement for every Pandas workflow; choose based on workload and integrations.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 2. Eager DataFrames and expression API
`pl.DataFrame` constructs an eager frame. `select` returns selected/computed columns; `with_columns` adds or replaces; `filter` keeps rows; `group_by().agg()` aggregates; `sort` orders. Expressions: `pl.col`, `pl.lit`, `.cast`, `.alias`, `.sum`, `.mean`, `.is_null`, `.fill_null`, string expressions. Expressions describe work performed by a DataFrame operation.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 3. Lazy execution
`scan_csv(path)` creates a lazy source; `filter` and `select` build a plan. `collect()` executes/materializes; `explain()` displays the plan. Projection and predicate pushdown may avoid loading unnecessary columns/rows. Lazy mode is useful for multi-step pipelines; eager mode is convenient for small data. Benchmark on representative data.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 4. Nulls, NaNs, and conversions
Polars distinguishes null from floating-point NaN. Use `.is_null`/`.fill_null` for nulls and `.is_nan`/`.fill_nan` for NaN. Convert with `.to_pandas()` or `.to_arrow()` when required; conversion may add memory/time cost. PyArrow is required for some Arrow interoperability paths.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

## Material allocation
| Notebook | Approximate effort | Coverage |
|---|---:|---|
| Concepts and Theory | 45–75 min | All subtopics, terminology, parameter reference, function variations, limitations, demonstrations. |
| Step-by-Step Tutorial | 45–75 min | Guided 1 — Compare eager and lazy; Guided 2 — Filter and derive a column; Guided 3 — Aggregate lazily; Guided 4 — Inspect Arrow schema |
| Practical Lab and Exercises | 60–120 min | Scenario, tasks, worked reference solution, and an extension challenge. |

## Practical lab brief
Reproduce a Pandas sales aggregation with Polars. Compare expression style and lazy execution.

### Required tasks
- Read sales.csv with Polars.
- Create a derived profit column.
- Filter high-value orders.
- Aggregate revenue by region lazily.
- Convert to Arrow and inspect the schema.

### Extension challenge
Benchmark Polars lazy scanning against Pandas eager loading on a large generated CSV. Control for warm-up, input size, and memory. Explain why one benchmark cannot prove universal superiority.

### References
- Polars guide: https://docs.pola.rs/
- Apache Arrow: https://arrow.apache.org/docs/
