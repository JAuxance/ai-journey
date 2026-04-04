# src — Pipeline Modules

Reusable code for loading, preparing, training, and evaluating the student performance model.

## Files

| File | Role |
|------|------|
| `data.py` | Load and clean the raw CSV dataset |
| `features.py` | Encode categorical columns and separate features from target |
| `train.py` | Instantiate and fit the chosen model |
| `evaluate.py` | Compute metrics (R2, CV scores) |
| `main.py` | Entry point that wires the full pipeline together |

## Model Selection

Four regression algorithms were compared on the same cleaned dataset and encoding pipeline to find the best fit for `Exam_Score`:

| Model | Notes |
|-------|-------|
| `LinearRegression` (LR) | **Best overall** — highest and most stable R2 across test and CV |
| `RandomForestRegressor` (RFR) | Lower CV mean than LR; more variance across folds |
| `GradientBoostingRegressor` (GBR) | Similar to RFR; did not outperform the linear baseline |
| `HistGradientBoostingRegressor` (Hist) | Faster than GBR but same conclusion — LR wins |

**Conclusion:** `LinearRegression` was selected as the final model. The dataset exhibits a predominantly linear structure, which means the added complexity of tree-based ensembles brings no measurable gain and reduces interpretability.