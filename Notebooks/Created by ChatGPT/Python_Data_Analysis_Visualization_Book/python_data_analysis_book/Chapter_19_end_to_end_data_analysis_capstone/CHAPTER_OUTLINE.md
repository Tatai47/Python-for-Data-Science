# Chapter 19 — End-to-End Data Analysis Capstone

**Purpose:** Combine file ingestion, validation, SQL, Pandas, statistics, visualization, machine learning, and communication into a reproducible portfolio project. Use the supplied synthetic sales/customer datasets.

**Prerequisites:** Completion of the earlier foundations, processing, database, visualization, and analysis chapters.

## Learning goals
- Design a complete analytical workflow from a business question.
- Load, validate, clean, and join multiple data sources.
- Create reproducible metrics and statistical analyses.
- Build visual findings and a simple predictive baseline.
- Deliver a documented notebook, exported outputs, and dashboard-ready dataset.

## Topic and subtopic plan
### 1. Project brief and analytical questions
The fictional business wants to understand revenue and profit patterns by region, product, customer segment, and time. Define decisions the analysis could inform, not just charts to produce. Establish the unit of analysis, metric definitions, reporting period, and exclusions before computing results.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 2. Data integration and validation
Load order-level sales, customer reference data, and optional JSON metadata. Check key uniqueness, referential integrity, valid dates, non-negative units, financial arithmetic, and missingness. Join on explicit keys and verify expected row counts after each join. Avoid many-to-many joins unless that relationship is intended.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 3. Metric design
Define revenue, gross profit, profit margin, order count, units sold, average order value, and customer counts. Distinguish sum of row-level margin from ratio of totals. Define time granularity, currency, handling of refunds, and denominator for each rate. Store metric calculations in reusable functions.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 4. Statistical reasoning
Use descriptive summaries and uncertainty intervals to distinguish large samples from stable patterns. Explore relationships, inspect group distributions, and test pre-specified comparisons. Avoid multiple unplanned tests and causal claims from observational records. Include practical effect magnitude and uncertainty.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 5. Visualization and narrative
Build a compact executive view, detailed diagnostic charts, and a data-quality section. Label axes with units, use appropriate aggregation, avoid misleading truncated scales, and annotate sample sizes. Write a headline, evidence, caveat, and action implication for each finding.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 6. Reproducibility and handoff
The final project should run from a clean environment, use relative paths, declare dependencies, avoid secrets, and preserve raw source files. Export a cleaned dataset, summary tables, charts, and a concise report. Include a README explaining data provenance, definitions, run order, limitations, and next steps.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

## Material allocation
| Notebook | Approximate effort | Coverage |
|---|---:|---|
| Concepts and Theory | 45–75 min | All subtopics, terminology, parameter reference, function variations, limitations, demonstrations. |
| Step-by-Step Tutorial | 45–75 min | Load and validate the project datasets; Join customer attributes; Create business metrics; Create a time-series summary; Visualize and export results; Optional SQL aggregation with SQLite |
| Practical Lab and Exercises | 60–120 min | Scenario, tasks, worked reference solution, and an extension challenge. |

## Practical lab brief
Prepare an analyst-ready sales performance report for management. Use the included orders and customer datasets, with transparent metrics, reproducible data-quality checks, and visual evidence.

### Required tasks
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

### Extension challenge
Extend the project with a monthly cohort view, customer retention definition, forecast baseline, model monitoring plan, automated quality tests, and a Streamlit application. State which conclusions are descriptive, predictive, or causal—and justify each label.

### References
- Pandas merge: https://pandas.pydata.org/docs/user_guide/merging.html
- Scikit-learn model evaluation: https://scikit-learn.org/stable/modules/model_evaluation.html
- Streamlit docs: https://docs.streamlit.io/
