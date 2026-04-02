# 00 Foundations

This section covers the essential basics before moving on to machine learning.

---

## Content

### NumPy

Folder: `numpy/`

**Learning journal** (`numpy_journal.py`)

A Python file structured into sections that traces everything explored:

1. **Basics** — array attributes: `shape`, `ndim`, `size`, `dtype`
2. **Copy** — independent copy with `np.copy()`
3. **Array Creation** — `np.array()`, `np.arange()`, `np.linspace()`, `np.ones()`, `np.empty()`, `np.sort()`, `np.concatenate()`
4. **Reshape And Axes** — `np.reshape()`, `np.newaxis`, `np.expand_dims()`
5. **Indexing Slicing Masks** — indexing, slicing, boolean masks, `np.nonzero()`
6. **Stack And Split** — `np.vstack()`, `np.hstack()`, `np.hsplit()`
7. **Operations And Matrices** — element-wise operations, `sum(axis=...)`, `.T`, `np.unique()`, `np.flip()`, random numbers with `np.random.default_rng()`
8. **Reshaping and flattening** — difference between `flatten()` (copy) and `ravel()` (view)

**Notes** (`numpy/notes.md`)

Personal observations on what is understood, what still feels unclear, and the learning approach used.

---

### NumPy Knowledge Test

Folder: `numpy/knowlege_test/`

- `numpy_knowledge_test.md` — 20-point test covering all concepts from the journal
- `exo.py` — code answers to the practical exercises in the test
- `feedback/numpy_knowledge_test_feedback.md` — full correction with per-exercise feedback (**final score: 15 / 20**)
- `review/numpy_topics_to_review.md` — list of topics to revisit following the test

**Strengths identified:** indexing, `reshape`, `flatten` vs `ravel`, `vstack`/`hstack`

**Topics to review:** boolean mask syntax, `axis=0` vs `axis=1` behavior, `np.nonzero()`, `.T`

---

### Pandas

Folder: `pandas/`

**Learning journal** (`pandas_journal.py`)

A Python file structured into sections that traces everything explored:

1. **Series** — 1D labeled array, NaN behavior forcing `float64` dtype
2. **DataFrame Creation** — from NumPy array with `DatetimeIndex`, from dict with mixed types
3. **Viewing Data** — `head()`, `tail()`, `index`, `columns`, `to_numpy()`
4. **Custom Index And Concat** — string index, adding rows with `pd.concat()`
5. **Reading CSV And JSON** — `pd.read_csv()`, `pd.read_json()`, label-based access with `loc`
6. **Operations And GroupBy** — `mean()`, `sum()`, `max()`, `groupby()` with aggregations
7. **Data Cleaning** — `drop()`, `dropna()`, `fillna()`, `replace()` for inconsistent values
8. **Manipulation** — `iloc` vs `loc`, boolean filtering, `fillna()`
9. **DataFrame Info** — `info()`, `describe()` for a full statistical overview
10. **Sorting Data** — `sort_values()`, `reset_index()`, adding computed columns
11. **Encoding Categorical Data** — `pd.get_dummies()` for one-hot encoding

---

### Matplotlib

Folder: `matplotlib/`

**Learning journal** (`matplotlib_journal.py`)

A Python file structured into sections that traces everything explored:

1. **Line Chart** — multiple lines, custom markers via style dict, grid, axis labels, tick positions
2. **Bar Chart** — vertical bar chart with categorical x-axis labels
3. **Pie Chart** — `autopct`, `explode`, `startangle`
4. **Scatter Chart** — two datasets, `s` (size), `label`, `legend`
5. **Histogram** — `np.random.normal()`, `np.clip()`, `bins`, custom colors
6. **Figure and Axes** — `plt.subplots(2, 3)`, individual axes configuration, `tight_layout()`
7. **CSV Chart** — horizontal bar chart from a Pokémon CSV (`value_counts()`, `barh`)
8. **Heatmap** — correlation matrix with `plt.imshow()`, `colorbar`, `coolwarm` colormap, `xticks` rotation
