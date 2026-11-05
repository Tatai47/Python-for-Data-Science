# Chapter 17 — Machine Learning with Scikit-learn

**Purpose:** Scikit-learn provides a consistent API for preprocessing, model fitting, evaluation, and model selection. Learn the end-to-end supervised-learning workflow while avoiding leakage and overclaiming.

**Prerequisites:** Python, NumPy, Pandas, descriptive statistics, and basic train/test reasoning.

## Learning goals
- Define features, target, task type, and a baseline.
- Split data before fitting transformations.
- Build preprocessing and estimator pipelines.
- Train regression and classification models.
- Evaluate with task-appropriate metrics and cross-validation.
- Recognize leakage, overfitting, and reproducibility requirements.

## Topic and subtopic plan
### 1. Estimator API
Most estimators follow `fit(X, y)`, `predict(X)`, and sometimes `predict_proba(X)`. Transformers expose `fit`, `transform`, and `fit_transform`. `get_params()` inspects hyperparameters; `set_params()` changes them. Inputs are commonly arrays or DataFrames with rows as samples and columns as features; preserve feature names where possible.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 2. Splitting and leakage
`train_test_split(X,y,test_size,train_size,random_state,shuffle,stratify)` separates data. Split before fitting imputation, scaling, feature selection, or encoders. Leakage occurs when information unavailable at prediction time enters training, including preprocessing fitted on all rows and future time information. For grouped or temporal data use group/time-aware splitters, not random splitting.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 3. Preprocessing and pipelines
`SimpleImputer(strategy=...)` fills missing values; `StandardScaler` centers/scales; `OneHotEncoder(handle_unknown="ignore")` encodes categories. `ColumnTransformer` applies transformations to subsets of columns. `Pipeline(steps=[...])` chains steps and fits them inside each validation fold, reducing leakage risk. Sparse/dense output depends on encoder configuration and data.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 4. Regression and classification
Regression targets are numeric; common baselines include `DummyRegressor`, `LinearRegression`, and tree-based regressors. Classification predicts classes; models include `LogisticRegression`, decision trees, random forests, and support vector machines. Classification probabilities require calibration checks before high-stakes threshold decisions.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 5. Evaluation metrics
Regression: MAE, MSE/RMSE, and R-squared; interpret units and outlier sensitivity. Classification: confusion matrix, accuracy, precision, recall, F1, ROC-AUC, and PR-AUC. Metrics depend on class balance and decision thresholds. Always compare with a baseline and report the data split and evaluation sample.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 6. Cross-validation and tuning
`cross_val_score` estimates performance across folds. `GridSearchCV` and `RandomizedSearchCV` tune parameters; their search must be conducted within training data, leaving a final test set untouched. `scoring` determines the metric; `cv` determines fold strategy. Set random seeds where applicable and record versions.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

## Material allocation
| Notebook | Approximate effort | Coverage |
|---|---:|---|
| Concepts and Theory | 45–75 min | All subtopics, terminology, parameter reference, function variations, limitations, demonstrations. |
| Step-by-Step Tutorial | 45–75 min | Guided 1 — Define target and baseline; Guided 2 — Fit and evaluate a linear model; Guided 3 — Compare with cross-validation; Guided 4 — Inspect residuals |
| Practical Lab and Exercises | 60–120 min | Scenario, tasks, worked reference solution, and an extension challenge. |

## Practical lab brief
Build a leakage-aware regression workflow for order revenue and a separate classification workflow using a built-in Scikit-learn dataset. Report baselines, preprocessing, metrics, and limitations.

### Required tasks
- Define feature columns and target.
- Create a reproducible train/test split.
- Fit a DummyRegressor baseline and a LinearRegression model.
- Build a mixed numeric/categorical Pipeline with ColumnTransformer.
- Evaluate using MAE, RMSE, and R-squared.
- Run cross-validation and tune a model using training data only.
- Explain at least two possible leakage paths.

### Extension challenge
Use a time-aware split with order_date, create features that would genuinely be known at prediction time, compare a tree ensemble with a linear baseline, and explain how an apparently strong feature could leak the target.

### References
- Scikit-learn user guide: https://scikit-learn.org/stable/user_guide.html
- Common pitfalls and leakage: https://scikit-learn.org/stable/common_pitfalls.html
