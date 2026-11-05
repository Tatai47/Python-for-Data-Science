# Chapter 01 — Python Foundations for Data Work

**Purpose:** Python is the programming layer underneath the data stack. Learn the language features needed to read data, transform values, automate work, and write reliable scripts.

**Prerequisites:** No previous programming experience; Python 3.10+ recommended.

## Learning goals
- Distinguish names, objects, values, and types.
- Choose appropriate built-in data structures.
- Use control flow, comprehensions, and functions for data tasks.
- Handle errors and organize reusable code.

## Topic and subtopic plan
### 1. Names, objects, and types
A name refers to an object. Assignment binds a name to an object; it does not copy it. Python is dynamically typed. Core scalar types are `int`, `float`, `bool`, `str`, and `NoneType`. `type(x)` reports an exact type; `isinstance(x, T)` also recognizes subclasses. `True == 1` is true, although `type(True) is int` is false.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 2. Mutable and immutable objects
Immutable examples include numbers, strings, and tuples; mutable examples include lists, dictionaries, and sets. `b = a` creates another reference. `a.copy()` makes a shallow copy; nested mutable objects remain shared. `copy.deepcopy()` recursively copies nested objects and may be costly.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 3. Containers and operations
Lists are ordered and mutable; tuples are ordered and immutable; dictionaries map hashable keys to values; sets contain unique hashable values. `append(x)` adds one list item; `extend(iterable)` adds many. `dict.get(key, default)` avoids `KeyError`. `set.add` and `set.update` add one and many values respectively.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 4. Control flow and comprehensions
`if/elif/else` select branches. `for` traverses an iterable; `while` repeats while a condition is true. `break`, `continue`, and `pass` control loops. List comprehensions use `[expression for item in iterable if condition]`; dictionary and set comprehensions use braces. Prefer a loop when branching or side effects become complex.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 5. Functions and arguments
`def f(required, optional=default, *args, **kwargs)` supports positional, defaulted, variable-length positional, and keyword arguments. `/` marks positional-only parameters; `*` marks keyword-only parameters. Avoid mutable defaults. A function without `return` returns `None`. Pass inputs explicitly and return results rather than depending on global variables.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 6. Errors, files, and modules
Use narrow `try/except` blocks and catch exceptions you can handle. `else` runs on success; `finally` runs during cleanup. Prefer `pathlib.Path` and context-managed files. Split reusable code into modules; `if __name__ == "__main__":` separates script execution from imports.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

## Material allocation
| Notebook | Approximate effort | Coverage |
|---|---:|---|
| Concepts and Theory | 45–75 min | All subtopics, terminology, parameter reference, function variations, limitations, demonstrations. |
| Step-by-Step Tutorial | 45–75 min | Guided 1 — Summarize a list; Guided 2 — Pair sequences; Guided 3 — Validate inputs; Guided 4 — Work safely with files |
| Practical Lab and Exercises | 60–120 min | Scenario, tasks, worked reference solution, and an extension challenge. |

## Practical lab brief
Build a reusable student-mark report. Validate the sequence, calculate summary statistics, count passes, and return the top three marks.

### Required tasks
- Write `summarise_marks(marks, pass_mark=40)`.
- Reject empty inputs and non-numeric values.
- Return count, average, highest, lowest, pass_count, and top_three.
- Test one edge case as well as the default case.

### Extension challenge
Add a keyword-only `round_to` argument and an optional minimum-score filter. Test empty input, text input, a single mark, and values exactly at the pass threshold.

### References
- Python tutorial: https://docs.python.org/3/tutorial/
- Built-in functions: https://docs.python.org/3/library/functions.html
- Pathlib: https://docs.python.org/3/library/pathlib.html
