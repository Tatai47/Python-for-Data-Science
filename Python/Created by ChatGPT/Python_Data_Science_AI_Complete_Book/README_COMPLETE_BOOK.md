# Python Data Science, Machine Learning & AI — Complete Notebook Book

This package extends the original Python-for-MBA/Data-Analyst course with 31 advanced chapters covering:

- Data Science
- Machine Learning
- AutoML
- Deep Learning
- Natural Language Processing

## Structure

Chapters 01–13 are preserved from the original archive. Chapters 14–44 add the new technologies requested.

Each chapter folder contains a clearly named Jupyter notebook. The notebooks are designed as teaching chapters with:

1. Learning objectives
2. Core concepts
3. Worked examples
4. Exercises
5. A mini-project
6. Practical notes where relevant

## New chapter map

### Data Science
14. NumPy Advanced
15. Pandas Advanced
16. Polars
17. Matplotlib Advanced
18. Seaborn
19. Plotly
20. Scikit-learn production workflows
21. Streamlit
22. Pydantic

### Machine Learning
23. LightGBM
24. XGBoost
25. CatBoost
26. Statsmodels
27. RAPIDS.ai (cuDF/cuML)
28. Optuna

### AutoML
29. PyCaret
30. H2O AutoML
31. Auto-sklearn
32. FLAML
33. AutoGluon

### Deep Learning
34. TensorFlow
35. PyTorch
36. fastai
37. Keras
38. PyTorch Lightning
39. JAX

### NLP
40. spaCy
41. Hugging Face Transformers
42. LangChain
43. LlamaIndex
44. ChromaDB

## Environment

The course spans packages with very different system requirements. Use the included requirements files as starting points and install GPU/framework-specific stacks separately when necessary.

Recommended baseline: Python 3.11.

For reproducible teaching environments, pin versions after validating them on your target OS. GPU frameworks such as RAPIDS, TensorFlow, PyTorch, JAX and some AutoML packages require platform-specific installation.

## Important

Some notebooks intentionally use commented examples for heavy or environment-dependent libraries. This keeps the book readable and avoids pretending that a CPU-only environment can run GPU-specific code.

## Suggested learning path

**Beginner:** 01–13 → 14–22

**Applied ML:** 23–28

**AutoML:** 29–33

**Deep Learning:** 34–39

**NLP / LLM applications:** 40–44

**Capstone recommendation:** Choose one business dataset and apply the complete pipeline from data validation and EDA through model selection, optimization, deployment, and retrieval/LLM components where relevant.
