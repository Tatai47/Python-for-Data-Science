# Chapter 12 — Seaborn: Statistical Data Visualization

**Purpose:** Seaborn builds statistical graphics on Matplotlib with high-level functions, semantic mappings, statistical estimators, and attractive defaults.

**Prerequisites:** Pandas DataFrames and basic Matplotlib; install Seaborn.

## Learning goals
- Understand long-form and wide-form data.
- Use axes-level and figure-level plotting functions.
- Create distribution, relational, categorical, and matrix plots.
- Interpret hue, facets, estimators, and confidence intervals.

## Topic and subtopic plan
### 1. Data model and semantics
Seaborn supports long and wide data; long form is usually clearer. Map with `data`, `x`, `y`, `hue`, `style`, and `size`. `hue` encodes categorical color, `style` marker/line type, and `size` a quantitative channel. Axes-level functions draw on a Matplotlib Axes (`scatterplot`, `histplot`, `boxplot`); figure-level functions manage grids (`relplot`, `displot`, `catplot`, `pairplot`).
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 2. Relational plots
`scatterplot(data,x,y,hue,style,size,alpha,...)` maps pairs. `lineplot` aggregates repeated observations by default and may show uncertainty; set `estimator=None` for raw lines. Confidence intervals around an estimate express uncertainty in an estimated statistic, not the range of individual values.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 3. Distribution plots
`histplot(data,x,bins="auto",stat="count",kde=False,...)` displays binned values. `kdeplot` estimates smooth density; bandwidth affects shape. `ecdfplot` shows the empirical cumulative distribution. `stat="density"` normalizes area rather than counts. Use consistent bins/scales for comparisons.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 4. Categorical plots
`barplot` estimates a statistic (mean by default); `countplot` counts observations. `boxplot` shows quartiles and whisker rules (`whis`); `violinplot` adds density; `stripplot`/`swarmplot` show observations. A mean bar is not a raw count. Consider median and spread where distributions are skewed.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 5. Heatmaps, pair plots, facets
`heatmap(data,annot,fmt,cmap,center,vmin,vmax)` maps matrix values to color. Correlation heatmaps show linear association, not causation. `pairplot(data,hue,vars,diag_kind)` can be expensive with many columns. Figure-level plots support row/column facets for small multiples.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

## Material allocation
| Notebook | Approximate effort | Coverage |
|---|---:|---|
| Concepts and Theory | 45–75 min | All subtopics, terminology, parameter reference, function variations, limitations, demonstrations. |
| Step-by-Step Tutorial | 45–75 min | Guided 1 — Compare distributions; Guided 2 — Examine numeric association; Guided 3 — Compare group means and spread; Guided 4 — Check correlation |
| Practical Lab and Exercises | 60–120 min | Scenario, tasks, worked reference solution, and an extension challenge. |

## Practical lab brief
Create a statistical visual report using distributions, relationships, categorical comparisons, and correlation. Explain what each chart can and cannot establish.

### Required tasks
- Plot revenue distributions by region with comparable bins.
- Examine units versus revenue grouped by product.
- Compare mean profit by region and explain the estimator.
- Create a correlation heatmap and state one caveat.

### Extension challenge
Use `relplot` or `catplot` for small multiples. Compare median with mean profit and explain what changes.

### References
- Seaborn tutorial: https://seaborn.pydata.org/tutorial.html
- Seaborn API: https://seaborn.pydata.org/api.html
