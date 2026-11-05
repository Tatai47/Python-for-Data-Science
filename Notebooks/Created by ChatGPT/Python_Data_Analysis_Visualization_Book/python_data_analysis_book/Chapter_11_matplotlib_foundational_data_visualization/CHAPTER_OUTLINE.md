# Chapter 11 — Matplotlib: Foundational Data Visualization

**Purpose:** Matplotlib is the core plotting library. Learn figures, axes, plot types, labels, scales, legends, layout, and export controls.

**Prerequisites:** NumPy/Pandas basics; install Matplotlib.

## Learning goals
- Distinguish Figure and Axes objects.
- Create line, bar, scatter, histogram, and box plots.
- Control labels, scales, legends, grids, and layouts.
- Export charts with readable dimensions and resolution.

## Topic and subtopic plan
### 1. Figure and Axes
A Figure is the overall canvas; an Axes is one plotting area. Prefer `fig, ax = plt.subplots(...)`, then `ax.plot`, `ax.set_title`, and `ax.legend`. Stateful `plt` functions are quick shortcuts; the object-oriented API is easier for multi-panel charts and reusable functions.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 2. Figure construction
`plt.subplots(nrows=1,ncols=1,figsize=None,sharex=False,sharey=False,squeeze=True,layout=None)` returns a Figure and Axes. `figsize` uses inches; `sharex/sharey` synchronize axes; `squeeze=False` guarantees a 2-D axes array; `layout="constrained"` helps prevent clipping. Save via `fig.savefig(fname,dpi=...,bbox_inches="tight")`; close figures in loops.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 3. Chart methods
`ax.plot(x,y,marker,linestyle,linewidth,label)` shows trends; `bar`/`barh` compares categories; `scatter(x,y,s,c,alpha)` shows relationships; `hist(x,bins,density,cumulative)` shows distributions; `boxplot` shows quartiles and potential outliers. Select chart type based on variable types and the analytical question.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 4. Axes and annotations
Use `set_title`, `set_xlabel`, `set_ylabel`, `set_xlim`, `set_ylim`, `set_xscale`, `set_yscale`, `grid`, and `legend`. Log scales change visual interpretation; label them. Avoid misleading truncated axes and make units, periods, and denominator clear.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 5. Export and accessibility
`dpi` controls raster resolution; SVG/PDF are vector formats. Keep labels readable at the final size, check contrast, and do not encode critical meaning by color alone. Save the final figure after setting labels and layout.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

## Material allocation
| Notebook | Approximate effort | Coverage |
|---|---:|---|
| Concepts and Theory | 45–75 min | All subtopics, terminology, parameter reference, function variations, limitations, demonstrations. |
| Step-by-Step Tutorial | 45–75 min | Guided 1 — Compare regional revenue; Guided 2 — Examine a time trend; Guided 3 — Inspect profit distribution; Guided 4 — Export the final chart |
| Practical Lab and Exercises | 60–120 min | Scenario, tasks, worked reference solution, and an extension challenge. |

## Practical lab brief
Create a sales visual report with regional revenue, daily revenue, and profit distribution. Every chart must have a title, axes, units, and readable layout.

### Required tasks
- Aggregate regional revenue.
- Parse dates and plot daily revenue chronologically.
- Plot the distribution of profit.
- Save one chart as PNG and SVG.

### Extension challenge
Create a 2x2 dashboard with KPIs and a rolling average over daily revenue. Explain how window size changes the interpretation.

### References
- Matplotlib quick start: https://matplotlib.org/stable/users/explain/quick_start.html
- Pyplot API: https://matplotlib.org/stable/api/pyplot_summary.html
