# Chapter 02 — Jupyter Notebook and Reproducible Workflows

**Purpose:** Jupyter combines narrative, executable code, and saved outputs. Good notebook practice makes an analysis understandable, repeatable, reviewable, and shareable.

**Prerequisites:** Chapter 1 Python fundamentals; JupyterLab or Jupyter Notebook.

## Learning goals
- Explain kernels, cells, execution order, and notebook metadata.
- Use Markdown, code cells, magic commands, and rich display.
- Restart and run notebooks from a clean state.
- Control randomness and document dependencies.

## Topic and subtopic plan
### 1. Notebook architecture
An `.ipynb` notebook is a JSON document with ordered cells, metadata, and outputs. A kernel is the process that executes code and retains variables. Visible order and execution order can differ; `In [n]` records execution sequence. A cell that depends on hidden state may work only after a particular sequence of clicks. Restart and run all cells before sharing.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 2. Cell types and outputs
Code cells execute code; Markdown cells contain headings, prose, tables, links, and math; raw cells are passed through for specialized exporters. Outputs can be text streams, execution results, or rich display data (HTML, images, charts). `print()` creates text; a final expression is usually displayed automatically.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 3. IPython and magic commands
IPython adds `%time`, `%timeit`, `%run`, `%pwd`, `%matplotlib inline`, `%%time`, and `%%writefile`. Magics are an interactive IPython feature, not Python syntax in a regular `.py` file. `%timeit` repeats a short expression; one timing is not a reliable performance benchmark.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 4. Reproducibility
Record data source, assumptions, environment, and random seeds. `np.random.default_rng(seed)` gives a reproducible generator in a fixed compatible environment; a seed does not guarantee identical results across all library versions. Prefer project-relative paths, lock dependencies for production, and keep credentials outside notebooks.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 5. Professional notebook structure
Use: question and decision context; data description and grain; assumptions; imports/configuration; validation; analysis sections; conclusions/caveats; references. Keep one idea per cell, limit huge outputs, avoid hard-coded secrets, and move reusable functions into modules. Test with a clean kernel.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

## Material allocation
| Notebook | Approximate effort | Coverage |
|---|---:|---|
| Concepts and Theory | 45–75 min | All subtopics, terminology, parameter reference, function variations, limitations, demonstrations. |
| Step-by-Step Tutorial | 45–75 min | Guided 1 — Ask an analytical question; Guided 2 — Inspect the result; Guided 3 — Summarize and rank; Guided 4 — Write a defensible conclusion |
| Practical Lab and Exercises | 60–120 min | Scenario, tasks, worked reference solution, and an extension challenge. |

## Practical lab brief
Create a clean-kernel notebook analysis answering which region generated the highest sales revenue. Document data checks, metric definition, and a defensible conclusion.

### Required tasks
- Load the sales dataset using a project-relative path.
- Check row count, duplicate IDs, missing values, and date range.
- Summarize revenue by region.
- State one limitation and distinguish observation from explanation.

### Extension challenge
Export an executive summary to Markdown and compare total revenue with average revenue per order. Re-run after restarting the kernel.

### References
- Jupyter documentation: https://docs.jupyter.org/
- IPython documentation: https://ipython.readthedocs.io/
