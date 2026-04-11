# Linear Algebra

*Based on [Stanford CS229 materials](https://cs229.stanford.edu/section/cs229-linalg.pdf) — studying fundamental math concepts to build a solid understanding of AI.*

---

## Table of Contents

1. [Basic Matrix Notation](#basic-matrix-notation)
2. [Vector Notation](#vector-notation)
3. [Dot Product](#dot-product)
4. [Outer Product](#outer-product)
5. [Matrix-Vector Products](#matrix-vector-products)
6. [Matrix-Matrix Products](#matrix-matrix-products)
7. [Identity Matrix and Diagonal Matrices](#the-identity-matrix-and-diagonal-matrices)
8. [Transpose](#transpose)

---

## Basic Matrix Notation

Let $A \in \mathbb{R}^{m \times n}$.

- $m$ = number of rows
- $n$ = number of columns
- The entries of $A$ are real numbers

---

## Vector Notation

Let $x \in \mathbb{R}^n$.

An $n$-dimensional vector is represented as a column vector (matrix of size $n \times 1$):

$$x = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}$$

---

## Dot Product

### Definition

Given $x, y \in \mathbb{R}^n$, the dot product is defined as:

$$x^T y = \sum_{i=1}^{n} x_i y_i$$

### Intuition

The dot product measures similarity between two vectors:

- positive → same direction
- zero → orthogonal
- negative → opposite direction

### Example

$$x = \begin{bmatrix} 1 \\ 2 \\ 4 \\ 5 \end{bmatrix}, \quad y = \begin{bmatrix} 1 \\ 3 \\ 4 \\ -5 \end{bmatrix}$$

$$x^T y = \begin{bmatrix} 1 & 2 & 4 & 5 \end{bmatrix} \begin{bmatrix} 1 \\ 3 \\ 4 \\ -5 \end{bmatrix} = -2$$

### Calculation

$$1 \cdot 1 + 2 \cdot 3 + 4 \cdot 4 + 5 \cdot (-5) = 1 + 6 + 16 - 25 = -2$$

---

## Outer Product

### Definition

Given $x \in \mathbb{R}^m$ and $y \in \mathbb{R}^n$, the outer product is defined as:

$$xy^T \in \mathbb{R}^{m \times n}, \quad (xy^T)_{ij} = x_i y_j$$

### Intuition

The outer product builds a matrix where each entry is the product of one component of $x$ and one component of $y$.
Each row is a scaled version of $y^T$.

### Example

$$x = \begin{bmatrix} 20 \\ 32 \\ 23 \end{bmatrix}, \quad y = \begin{bmatrix} 53 \\ 28 \\ 76 \end{bmatrix}$$

$$xy^T = \begin{bmatrix} 20 \\ 32 \\ 23 \end{bmatrix} \begin{bmatrix} 53 & 28 & 76 \end{bmatrix} = \begin{bmatrix} 20 \cdot 53 & 20 \cdot 28 & 20 \cdot 76 \\ 32 \cdot 53 & 32 \cdot 28 & 32 \cdot 76 \\ 23 \cdot 53 & 23 \cdot 28 & 23 \cdot 76 \end{bmatrix} = \begin{bmatrix} 1060 & 560 & 1520 \\ 1696 & 896 & 2432 \\ 1219 & 644 & 1748 \end{bmatrix}$$

---

## Matrix-Vector Products

### Definition

Given a matrix $A \in \mathbb{R}^{m \times n}$ and a vector $x \in \mathbb{R}^n$, their product is a vector $y = Ax \in \mathbb{R}^m$:

$$y = Ax = \begin{bmatrix} a_1^T \\ a_2^T \\ \vdots \\ a_m^T \end{bmatrix} x = \begin{bmatrix} a_1^T x \\ a_2^T x \\ \vdots \\ a_m^T x \end{bmatrix}$$

### Intuition

The matrix-vector product transforms a vector into another vector.
Each entry of the result is the dot product between one row of the matrix and the vector.

### Example

$$A = \begin{bmatrix} 1 & 2 & 4 \\ 2 & 3 & 5 \\ 3 & 10 & 8 \end{bmatrix}, \quad x = \begin{bmatrix} 3 \\ 4 \\ 4 \end{bmatrix}, \quad y = Ax = \begin{bmatrix} 27 \\ 38 \\ 81 \end{bmatrix}$$

### Calculation

$$a_1^T x = 1 \cdot 3 + 2 \cdot 4 + 4 \cdot 4 = 27$$

$$a_2^T x = 2 \cdot 3 + 3 \cdot 4 + 5 \cdot 4 = 38$$

$$a_3^T x = 3 \cdot 3 + 10 \cdot 4 + 8 \cdot 4 = 81$$

---

## Matrix-Matrix Products

### Definition

The product of two matrices is obtained by taking the dot product of each row of the first matrix with each column of the second matrix:

$$C_{ij} = a_i^T b_j = \sum_{k=1}^{n} A_{ik} B_{kj}$$

In full matrix form, where $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{n \times p}$:

$$C = AB = \begin{bmatrix} a_1^T b_1 & a_1^T b_2 & \cdots & a_1^T b_p \\ a_2^T b_1 & a_2^T b_2 & \cdots & a_2^T b_p \\ \vdots & \vdots & \ddots & \vdots \\ a_m^T b_1 & a_m^T b_2 & \cdots & a_m^T b_p \end{bmatrix}$$

### Intuition

Each entry of the product matrix tells us how much a row of $A$ aligns with a column of $B$.
Matrix multiplication combines rows and columns to produce new values that summarize their interactions.

### Example

$$A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}$$

$$AB = \begin{bmatrix} 1 \cdot 5 + 2 \cdot 7 & 1 \cdot 6 + 2 \cdot 8 \\ 3 \cdot 5 + 4 \cdot 7 & 3 \cdot 6 + 4 \cdot 8 \end{bmatrix} = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}$$

### Column and Row Views

In the outer product formulation $C = AB$:

- $a_i$ → i-th **column** of $A$
- $b_i^T$ → i-th **row** of $B$ (= i-th column of $B$, transposed)

Same data, different orientation.

### Interpretation

$C$ can also be expressed as a sum of outer products:

$$C = AB = \sum_{i=1}^{n} a_i b_i^T$$

where $a_i$ is the $i$-th column of $A$ and $b_i^T$ is the $i$-th row of $B$.

### Matrix-Matrix as Matrix-Vector Products

Each column of $C$ is $A$ multiplied by the corresponding column of $B$:

$$C = AB = \begin{bmatrix} Ab_1 & Ab_2 & \cdots & Ab_p \end{bmatrix}$$

So computing $AB$ = applying $A$ to each column of $B$.

---

## The Identity Matrix and Diagonal Matrices

### Identity Matrix

The identity matrix $I \in \mathbb{R}^{n \times n}$ has 1s on the diagonal and 0s everywhere else:

$$I_{ij} = \begin{cases} 1 & \text{if } i = j \\ 0 & \text{if } i \neq j \end{cases}$$

It is the "1" of matrix multiplication: $AI = A = IA$

In numpy: `np.eye(n)`

### Diagonal Matrix

A diagonal matrix $D = \text{diag}(d_1, d_2, \dots, d_n)$ has non-zero values only on the diagonal:

$$D_{ij} = \begin{cases} d_i & \text{if } i = j \\ 0 & \text{if } i \neq j \end{cases}$$

Note: $I = \text{diag}(1, 1, \dots, 1)$

In numpy: `np.diag([d1, d2, ..., dn])`

---

## Transpose

Flips rows and columns of a matrix. If $A \in \mathbb{R}^{m \times n}$, then $A^T \in \mathbb{R}^{n \times m}$:

$$(A^T)_{ij} = A_{ji}$$

In numpy: `A.T`

### Properties

- $(A^T)^T = A$ → double transpose = back to original
- $(AB)^T = B^T A^T$ → **order reverses**
- $(A + B)^T = A^T + B^T$ → distributes over addition

### Key Rule

$$( AB)^T = B^T A^T$$

```python
(B @ C).T == C.T @ B.T  # True
```
