# Chapter 13 — Interactive Visualization with Plotly, Bokeh, and Altair

**Purpose:** Interactive charts support hover, zoom, selection, and linked views. Compare three libraries and their interaction models.

**Prerequisites:** Pandas, Matplotlib concepts, and chart grammar; full stack includes Plotly, Bokeh, and Altair.

## Learning goals
- Build Plotly Express and Graph Objects charts.
- Understand Bokeh figures, glyphs, sources, and tools.
- Create declarative Altair charts and encodings.
- Choose a library based on interaction, deployment, performance, and fit.

## Topic and subtopic plan
### 1. Plotly Express and Graph Objects
Plotly Express (`px`) is a high-level API: `px.scatter(data_frame,x,y,color,size,hover_name,facet_col,...)`; other functions include `line`, `bar`, `histogram`, and `box`. Graph Objects (`go`) gives lower-level control with `go.Figure`, traces (`go.Scatter`, `go.Bar`), `update_layout`, and `update_traces`. Use Express for common charts and Graph Objects for trace-level control.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 2. Layout and interaction
A Plotly Figure has `data` traces and a `layout`. Use `update_layout(title,xaxis_title,yaxis_title,template)` and `update_traces(hovertemplate=...)`. `fig.show()` renders; `write_html(path,include_plotlyjs=...)` exports HTML. Give the default chart a useful view and hover fields; excessive interaction can add friction.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 3. Bokeh model
`figure()` creates a plot. Glyphs such as `line`, `circle`, `scatter`, and `vbar` add marks. `ColumnDataSource` provides named columns for linked selection and hover tools. Tools include pan, wheel zoom, box zoom, reset, save, and hover. Use `output_file`/`save` for HTML output or notebook output for inline rendering.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 4. Altair and chart grammar
Altair is declarative: `alt.Chart(data).mark_point().encode(x="units:Q",y="revenue:Q",color="region:N")`. Types: `Q` quantitative, `N` nominal, `O` ordinal, `T` temporal. Transforms include `transform_filter`, `transform_aggregate`, and `transform_calculate`. Parameters/selections drive interactive filters. Large datasets may encounter row limits.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 5. Library selection
Plotly has broad chart coverage and integrates with dashboard frameworks; Bokeh offers browser-oriented plot models and linked interactions; Altair provides concise declarative specifications. Evaluate deployment, accessibility, performance, maintainability, team skill, and offline behavior.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

## Material allocation
| Notebook | Approximate effort | Coverage |
|---|---:|---|
| Concepts and Theory | 45–75 min | All subtopics, terminology, parameter reference, function variations, limitations, demonstrations. |
| Step-by-Step Tutorial | 45–75 min | Guided 1 — Create a Plotly figure; Guided 2 — Customize a trace; Guided 3 — Add a Bokeh bar glyph; Guided 4 — Declare a chart with Altair |
| Practical Lab and Exercises | 60–120 min | Scenario, tasks, worked reference solution, and an extension challenge. |

## Practical lab brief
Build an interactive regional sales exploration using multiple libraries, then compare their syntax and interaction models.

### Required tasks
- Create a Plotly revenue bar chart with hover values.
- Create Graph Objects product-profit chart.
- Build Bokeh glyph visualization if installed.
- Build Altair scatter chart if installed.
- Select a library for a dashboard and justify the choice.

### Extension challenge
Add date-range filters and a linked selection. Export to HTML and verify the chart in a browser without a running notebook server.

### References
- Plotly: https://plotly.com/python/
- Bokeh: https://docs.bokeh.org/en/latest/docs/user_guide.html
- Altair: https://altair-viz.github.io/
