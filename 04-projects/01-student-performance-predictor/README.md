# Student Performance Predictor

## Objective
Predict `Exam_Score` from tabular student data and compare preprocessing strategies for a `LinearRegression` baseline.

## Project Structure
- `data/`: dataset files used by the project
- `notebooks/`: exploratory analysis and preprocessing experiments
- `src/`: reusable pipeline code for loading, preparing, training, and evaluating

## Workflow
1. Load the dataset from `data/StudentPerformanceFactors.csv`
2. Inspect missing values
3. Prepare features with different encoding strategies
4. Train a `LinearRegression` model
5. Evaluate the model with a fixed train/test split and 5-fold cross-validation
6. Compare results and summarize findings

## Notebook Comparison
The notebook `notebooks/01_eda.ipynb` now compares two controlled preprocessing versions on the same cleaned dataset after `dropna()`.

### Version 1: All Dummies
- Strategy: one-hot encode every categorical column with `drop_first=True`
- Test `R2`: `0.7314`
- Mean CV `R2`: `0.7204`
- CV standard deviation: `0.0696`

### Version 2: Mixed Encoding
- Strategy: ordinal encode ordered categories such as `Low / Medium / High` and `Near / Moderate / Far`, then one-hot encode nominal columns
- Test `R2`: `0.7324`
- Mean CV `R2`: `0.7207`
- CV standard deviation: `0.0695`

## Result
The controlled comparison shows that the two encoding strategies perform almost the same. The mixed encoding version is slightly better, but the gap is very small.

Earlier exploratory work in the notebook also produced a stronger one-hot encoded reference result with:
- Test `R2`: `0.7699`
- Mean CV `R2`: `0.7263`

That earlier score came from a different preprocessing setup, so it should be treated as an exploratory reference rather than a direct apples-to-apples comparison.

## Current Conclusion
- `LinearRegression` remains a strong baseline for this dataset
- preprocessing choices change the score, but not dramatically in the controlled comparison
- the model seems to capture mostly linear structure from the available features
