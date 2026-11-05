# Chapter 05 — NumPy: Numerical Computing

**Purpose:** NumPy provides homogeneous n-dimensional arrays and fast vectorized operations, forming the numerical foundation of the Python data ecosystem.

**Prerequisites:** Python lists, loops, functions, and arithmetic; install NumPy.

## Learning goals
- Explain ndarray shape, axes, dtype, and memory layout.
- Create, index, slice, reshape, and combine arrays.
- Use broadcasting, vectorized expressions, reductions, and masks.
- Handle missing numeric values and reproducible random sampling.

## Topic and subtopic plan
### 1. The ndarray model
A NumPy `ndarray` is a homogeneous n-dimensional array. Key attributes: `ndim`, `shape`, `size`, `dtype`, and `itemsize`. Homogeneous storage enables efficient numerical operations. A 1-D array has one axis; a 2-D array is commonly rows and columns. Numeric dtypes include signed/unsigned integers, floats, complex values, booleans, datetime/timedelta, and strings.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 2. Array creation
`np.array(object, dtype=None)` builds from array-like data. `zeros(shape)`, `ones(shape)`, and `full(shape, fill_value)` initialize arrays. `arange(start, stop, step)` builds a step-based range; `linspace(start, stop, num=50, endpoint=True)` creates a fixed number of evenly spaced values. `eye(N, M=None, k=0)` creates an identity-like matrix. Prefer `linspace` if the point count matters.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 3. Indexing, slicing, and views
Use `a[row, column]`; `a[:, 1]` selects a column. Slice stop is exclusive. Basic slices usually make views that share memory; advanced integer/boolean indexing usually returns copies. Use `.copy()` for independent values. Boolean masks select elements; combine comparisons with `&` and `|`, parenthesizing each condition. Do not use Python `and/or` on arrays.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 4. Shape changes and broadcasting
`reshape` changes shape while preserving element order; `-1` infers one dimension. `ravel()` returns a view where possible; `flatten()` copies. `.T` transposes 2-D arrays. `concatenate` joins along an existing axis; `stack` adds a new axis. Broadcasting compares trailing dimensions: they are compatible when equal or one is 1. `(n,1)` plus `(1,m)` yields `(n,m)`.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 5. Vectorization and reductions
Vectorization applies operations to whole arrays instead of Python loops. Reductions include `sum`, `mean`, `min`, `max`, and `std`; `axis=0` reduces rows, yielding per-column results; `axis=1` yields per-row results. `keepdims=True` preserves singleton dimensions for broadcasting. Prefer `np.random.default_rng(seed)`; methods include `integers`, `normal`, `random`, and `choice`.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 6. Missing values and precision
`np.nan` is a floating-point missing sentinel; NaN is unequal to itself. Use `isnan`, `nanmean`, and `nanmedian`. Integers cannot normally store NaN without changing dtype. Choose dtypes based on value range and precision requirements; floating point has finite precision, so avoid exact equality tests for computed decimal results.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

## Material allocation
| Notebook | Approximate effort | Coverage |
|---|---:|---|
| Concepts and Theory | 45–75 min | All subtopics, terminology, parameter reference, function variations, limitations, demonstrations. |
| Step-by-Step Tutorial | 45–75 min | Guided 1 — Create a mark matrix; Guided 2 — Calculate along the correct axis; Guided 3 — Use boolean masks; Guided 4 — Standardize columns |
| Practical Lab and Exercises | 60–120 min | Scenario, tasks, worked reference solution, and an extension challenge. |

## Practical lab brief
Analyze a matrix of student marks using NumPy only. Compute subject averages, student totals, pass status, and standardized scores.

### Required tasks
- Create a 2-D array with at least five students and three subjects.
- Calculate subject means and standard deviations along the correct axis.
- Build a mask for students who passed every subject.
- Standardize columns and verify approximate zero mean.

### Extension challenge
Compare population standard deviation (`ddof=0`) with sample standard deviation (`ddof=1`). Add a missing value and use NaN-aware functions.

### References
- NumPy absolute beginners: https://numpy.org/doc/stable/user/absolute_beginners.html
- NumPy reference: https://numpy.org/doc/stable/reference/
