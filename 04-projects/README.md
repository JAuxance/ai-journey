# 04 Projects

This section contains end-to-end portfolio projects built to practice the full machine learning workflow: data exploration, feature engineering, modelling, evaluation, and interpretation.

---

## Content

### Student Performance Predictor

Folder: `01-student-performance-predictor/`

**Context**

The dataset contains 6 607 student records with 19 features covering study habits, school environment, and personal background: hours studied, attendance rate, parental involvement, access to resources, sleep hours, previous scores, motivation level, tutoring sessions, family income, teacher quality, peer influence, and more. The target variable is `Exam_Score`, a continuous score that the model tries to predict.

The project explores how much of the exam score variance can be explained by these factors with a simple linear model, and whether the way categorical features are encoded changes anything.

**Objective**

Predict `Exam_Score` from tabular student data and compare preprocessing strategies for a `LinearRegression` baseline.

**Data**

- `data/StudentPerformanceFactors.csv` — main dataset used across all notebooks and the pipeline

**Notebooks**

- `notebooks/01_eda_one_hot.ipynb` — exploratory analysis with full one-hot encoding (`drop_first=True`) on every categorical column
- `notebooks/02_eda_mixed_encoding.ipynb` — same cleaned dataset but ordered categories such as `Low / Medium / High` and `Near / Moderate / Far` are ordinal-encoded instead

Both notebooks follow the same workflow:
1. Load and inspect the dataset
2. Drop rows with missing values
3. Prepare features with the chosen encoding strategy
4. Train a `LinearRegression` model
5. Evaluate with a fixed train/test split and 5-fold cross-validation

**Pipeline** (`src/`)

Reusable modules that mirror the notebook workflow:
- `data.py` — dataset loading
- `features.py` — feature preparation and encoding
- `train.py` — model training
- `evaluate.py` — evaluation metrics and cross-validation
- `main.py` — end-to-end entry point

**Results**

| Strategy         | Test R² | Mean CV R² | CV Std |
|------------------|---------|------------|--------|
| One-hot encoding | 0.7314  | 0.7204     | 0.0696 |
| Mixed encoding   | 0.7324  | 0.7207     | 0.0695 |

**Conclusion**

`LinearRegression` is a strong baseline for this dataset. The two encoding strategies produce nearly identical scores, suggesting the model captures mostly linear structure from the available features. Preprocessing choices matter, but the gap between strategies is small in a controlled comparison.