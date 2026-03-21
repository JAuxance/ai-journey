## My Current Learning Context

I am learning by experimenting first and organizing my code after.
Right now, this works well for me because I can explore freely, make mistakes, compare results, and then turn that into something clearer.

At this stage, I have mainly worked on NumPy basics:
- creating arrays
- reading `shape`, `ndim`, `size`, and `dtype`
- copying arrays
- reshaping arrays
- adding a new axis
- indexing and slicing
- using boolean masks
- stacking and splitting arrays
- transposing arrays
- getting unique values
- doing simple array operations

## What I Practiced

I practiced creating arrays with:
- `np.array()`
- `np.arange()`
- `np.linspace()`
- `np.ones()`
- `np.empty()`

I also practiced:
- sorting with `np.sort()`
- concatenating with `np.concatenate()`
- reshaping with `np.reshape()`
- adding axes with `np.newaxis` and `np.expand_dims()`
- selecting values with indexing, slicing, and masks
- using `np.vstack()`, `np.hstack()`, and `np.hsplit()`
- summing rows and columns with `sum(axis=...)`
- transposing with `.T`
- getting unique values with `np.unique()`
- reversing part of a matrix with `np.flip()`

## What I Understand Better Now

I understand better that:
- `shape` describes the structure of the array
- `ndim` tells me how many dimensions the array has
- `size` gives the total number of elements
- `len(shape) == ndim`
- `size == product(shape)`
- a real copy is independent from the original array
- `reshape()` changes the form of the array but not the total number of elements
- `np.newaxis` and `expand_dims()` help me turn a 1D array into a row or a column
- masks let me filter values based on a condition
- `axis=0` and `axis=1` do not mean the same thing, especially for sums and matrix operations

## What Still Feels In Progress

I am not trying to pretend I fully know everything yet.
Some ideas still feel in progress and I want to keep practicing them:
- the difference between a copy and a view
- when a slice changes the original array
- how `axis` really behaves in more situations
- transposing and reshaping matrices without confusion
- getting unique items with counts, not just unique values

## My Working Method

For now, my method is:
1. I test ideas quickly in code.
2. I let myself write things in one flow.
3. I reorganize the result after.
4. I keep a cleaner version as a learning trace.

This feels more natural for me than trying to write everything clean from the start.
