# 02 Machine Learning

This section documents the first machine learning experiments built with scikit-learn.

---

## Content

### Scikit-Learn

Folder: `02-machine-learning/`

**Learning journal** (`sklearn_journal.ipynb`)

A notebook structured into sections that traces the full workflow of a first regression project:

1. **Data Preparation** - loading the Pokemon dataset from `data/pokemon.csv`, filling missing values in `Type 2`, and encoding categorical columns with `pd.get_dummies()`
2. **Features And Target** - selecting `HP`, `Defense`, `Sp. Atk`, `Sp. Def`, and `Speed` as input features to predict `Attack`
3. **Model Training And Evaluation** - splitting the dataset with `train_test_split()`, running `GridSearchCV` on a `RandomForestRegressor`, and measuring performance with `r2_score`
4. **Model Persistence** - saving the trained model to `models/pokemon.pkl` with `joblib.dump()`
5. **Prediction Chart** - plotting real vs predicted values with Matplotlib and adding an ideal reference line

**Data files**

- `data/pokemon.csv` - main dataset used in the notebook
- `data/pokemon.json` - additional Pokemon data file kept in the project

**Saved model**

- `models/pokemon.pkl` - trained regression model generated from the notebook
