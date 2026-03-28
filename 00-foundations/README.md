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
