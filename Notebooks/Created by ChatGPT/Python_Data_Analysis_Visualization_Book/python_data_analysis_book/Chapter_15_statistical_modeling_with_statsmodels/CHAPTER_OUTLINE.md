# Chapter 15 — Statistical Modeling with Statsmodels

**Purpose:** Statsmodels provides interpretable statistical models with coefficient estimates, uncertainty measures, diagnostics, and formal inference. Learn linear regression, categorical predictors, residual analysis, and time-series foundations.

**Prerequisites:** Pandas, NumPy, descriptive statistics, and basic probability; SciPy statistics is recommended.

## Learning goals
- Fit and interpret ordinary least squares regression.
- Use formulas and categorical variables safely.
- Interpret coefficients, confidence intervals, p-values, and model fit.
- Evaluate residual assumptions and recognize model limitations.
- Understand the introductory workflow for time-series analysis.

## Topic and subtopic plan
### 1. Model specification and design matrices
`statsmodels.api.OLS(endog, exog, missing="none")` fits a linear model; add an intercept explicitly with `sm.add_constant(X)`. Formula API `statsmodels.formula.api.ols("y ~ x1 + C(group)", data=df)` creates design matrices and handles categorical terms via `C()`. Formula operators include `+`, `:`, `*` (main effects plus interaction), and `-1` (remove intercept).
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 2. Fit and inspect an OLS model
`model.fit(cov_type="nonrobust")` estimates coefficients; common robust covariance options include `HC0`–`HC3`, which alter standard errors and inference, not fitted coefficients. `summary()` provides coefficient table, confidence intervals, R-squared, F-statistic, and diagnostics. A coefficient is conditional on the other included predictors and model specification.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 3. Inference and model fit
`params`, `bse`, `tvalues`, `pvalues`, `conf_int()`, `rsquared`, `rsquared_adj`, `fittedvalues`, and `resid` expose key results. R-squared is the fraction of outcome variation explained in-sample under the model definition; it does not establish causation, correct specification, or out-of-sample performance.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 4. Assumptions and diagnostics
Classical OLS inference relies on a suitable linear conditional mean, independent errors, and assumptions for standard errors (homoscedasticity for conventional covariance; normality for exact small-sample t/F inference). Inspect residual-versus-fitted plots, Q-Q plots, leverage, influence, multicollinearity, and time ordering. Heteroscedasticity-robust standard errors do not fix omitted-variable bias or nonlinear specification.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 5. Prediction and leakage
Separate training and test periods or samples when evaluating prediction. Confidence intervals for the mean response are narrower than prediction intervals for a new observation. Never use future information in predictors for a historical prediction task. Do not interpret observational regression coefficients as causal effects without a defensible identification strategy.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

### 6. Time-series entry points
Time series observations are ordered and often autocorrelated. Statsmodels includes ACF/PACF tools, ARIMA/SARIMAX, exponential smoothing, and decomposition. Split chronologically, inspect trend/seasonality, and avoid random train/test splits for forecasting. Check residual autocorrelation and compare against simple baselines.
**Depth target:** 2–4 notebook screens, including key terms, API/function forms, parameter meaning, examples, caveats, and a short check-for-understanding.

## Material allocation
| Notebook | Approximate effort | Coverage |
|---|---:|---|
| Concepts and Theory | 45–75 min | All subtopics, terminology, parameter reference, function variations, limitations, demonstrations. |
| Step-by-Step Tutorial | 45–75 min | Guided 1 — Define the model question; Guided 2 — Fit and read the coefficient table; Guided 3 — Diagnose residual structure; Guided 4 — Compare conventional and robust inference |
| Practical Lab and Exercises | 60–120 min | Scenario, tasks, worked reference solution, and an extension challenge. |

## Practical lab brief
Build an interpretable model of revenue using units, discount, and region. Explain the reference category, coefficient units, model fit, residual diagnostics, and limits of causal interpretation.

### Required tasks
- Fit `revenue ~ units + discount + C(region)`.
- Interpret the units and discount coefficients with units and caveats.
- Compare conventional and HC3 standard errors.
- Make a residual-versus-fitted plot and a Q-Q plot.
- Evaluate out-of-sample prediction separately from in-sample fit.

### Extension challenge
Add a units-by-discount interaction and compare it with the main-effects model using an appropriate nested model comparison. Check collinearity and explain why model fit alone cannot establish causality.

### References
- Statsmodels user guide: https://www.statsmodels.org/stable/user-guide.html
- Formula examples: https://www.statsmodels.org/stable/examples/index.html
