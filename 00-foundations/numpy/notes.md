# Algorithms Notes

## Where I Am Right Now

Right now I am learning by testing things first and organizing them after.
This feels natural to me because I can move fast, follow my curiosity, make mistakes, compare outputs, and only clean everything up once I start understanding the logic better.

At this point, most of what I have done is around NumPy basics and first manipulations.
I have already spent time on:
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
- doing simple operations on arrays and matrices

## What I Actually Tried

I tested several ways to create arrays:
- `np.array()`
- `np.arange()`
- `np.linspace()`
- `np.ones()`
- `np.empty()`

Then I started exploring transformations and operations:
- sorting with `np.sort()`
- concatenating with `np.concatenate()`
- reshaping with `np.reshape()`
- adding axes with `np.newaxis` and `np.expand_dims()`
- selecting values with indexing, slicing, and masks
- stacking with `np.vstack()` and `np.hstack()`
- splitting with `np.hsplit()`
- summing with `sum(axis=...)`
- transposing with `.T`
- getting unique values with `np.unique()`
- flipping part of a matrix with `np.flip()`

## What Is Becoming Clear

Some ideas are starting to feel more solid now.

I am seeing more clearly that:
- `shape` describes the structure of the array
- `ndim` tells me how many dimensions I am working with
- `size` gives the total number of elements
- `len(shape) == ndim`
- `size == product(shape)`
- a true copy is independent from the original array
- `reshape()` changes the form, not the total number of elements
- `np.newaxis` and `expand_dims()` help me turn a 1D array into a row or a column
- masks are a clean way to filter values with conditions
- `axis=0` and `axis=1` really matter and change how NumPy reads an operation

## What Still Feels Unfinished

I do not want these notes to pretend I already master everything.
Some parts still feel unfinished and I want to revisit them calmly:
- when slicing returns something linked to the original array
- how `axis` behaves in more cases
- transposing and reshaping matrices without hesitation
- getting unique items with counts, not only unique values

## How I Learn Best For Now

For now, my best method looks like this:
1. I test ideas quickly in code.
2. I let myself write in one flow.
3. I look at the output and compare what changes.
4. I reorganize the result after.
5. I keep a cleaner version as a trace of what I really understood.

This is not the cleanest method at the beginning, but for me it is one of the most honest ones.
It helps me see my real thinking before I polish it.
