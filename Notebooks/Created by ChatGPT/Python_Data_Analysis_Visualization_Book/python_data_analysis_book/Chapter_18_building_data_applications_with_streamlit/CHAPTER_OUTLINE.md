# Chapter 18 — Building Data Applications with Streamlit

**Purpose:** Streamlit turns Python scripts into interactive data applications. Learn the execution model, input widgets, caching, charts, data loading, secrets, and deployment considerations.

**Prerequisites:** Python, Pandas, and at least one visualization library; install Streamlit separately.

## Learning goals
- Explain Streamlit’s script rerun model.
- Build layouts with titles, columns, containers, and sidebar widgets.
- Use caching appropriately for data and resources.
- Connect CSV and MySQL data safely.
- Structure, test, and deploy a small analytical application.

## Topic and subtopic plan
### 1. Execution model and display API
A Streamlit app is a Python script run by `streamlit run app.py`. Widget interactions trigger a script rerun from top to bottom. Display functions include `st.title`, `header`, `subheader`, `write`, `markdown`, `dataframe`, `table`, `metric`, and chart methods such as `line_chart` and `plotly_chart`. Use a clear top-to-bottom flow and avoid expensive unguarded work on every rerun.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 2. Layout and widgets
`st.sidebar`, `st.columns`, `st.container`, `st.expander`, and `st.tabs` organize content. Widgets include `selectbox`, `multiselect`, `slider`, `date_input`, `text_input`, `number_input`, `checkbox`, `radio`, `file_uploader`, and `button`. Most return the current selection/value; `key` gives a stable identity. Widget state is managed by Streamlit and can be explicitly read through `st.session_state`.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 3. Caching and session state
`@st.cache_data` caches serializable data results and returns copies; `@st.cache_resource` caches shared resources such as database connections or ML models. Configure TTL, max entries, and hash behavior deliberately. `st.session_state` persists values across reruns for a user session. Caching must not expose one user’s private data to another; include user/security context in cache keys where relevant.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 4. Data sources and secrets
Use Pandas readers for uploaded CSV/Excel files. Database credentials belong in Streamlit secrets (`.streamlit/secrets.toml`) or environment variables, never committed source files. Use parameterized SQL, read-only credentials for dashboards, connection timeouts, and explicit error handling. Treat uploaded files as untrusted input and validate size, schema, and content.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 5. Application architecture and deployment
Separate loading, cleaning, metric calculation, and display functions. Use stable schemas and cache expensive read-only queries with a suitable TTL. Test filtering edge cases, missing data, empty results, and large inputs. Deploy with pinned dependencies, secrets management, resource limits, and a refresh strategy. The app script itself is the application; notebook cells are a learning environment.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

## Material allocation
| Notebook | Approximate effort | Coverage |
|---|---:|---|
| Concepts and Theory | 45–75 min | All subtopics, terminology, parameter reference, function variations, limitations, demonstrations. |
| Step-by-Step Tutorial | 45–75 min | Guided 1 — Define the app layout; Guided 2 — Add user controls; Guided 3 — Add KPIs and charts; Guided 4 — Run and test |
| Practical Lab and Exercises | 60–120 min | Scenario, tasks, worked reference solution, and an extension challenge. |

## Practical lab brief
Build a regional sales dashboard with filters, KPIs, a trend chart, a detail table, and an optional MySQL source. Separate reusable logic from UI components.

### Required tasks
- Create a Streamlit script with page configuration and title.
- Load sales.csv using a cached function.
- Add region and product filters.
- Display order count, revenue, and profit KPIs.
- Plot revenue over time and by region.
- Add a data table and CSV download.
- Document how to configure database secrets without committing credentials.

### Extension challenge
Add date filters, a Plotly chart, data-quality warnings, pagination or row limits, and a MySQL backend using secrets/environment variables. Test access control and cache isolation.

### References
- Streamlit documentation: https://docs.streamlit.io/
- Caching: https://docs.streamlit.io/develop/concepts/architecture/caching
