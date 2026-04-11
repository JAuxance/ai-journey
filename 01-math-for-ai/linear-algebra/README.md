# Linear Algebra

<i>I study fundamental math concepts <a href="cs229.stanford.edu/section/cs229-linalg.pdf">(based on Stanford materials)</a> to build a solid understanding of AI.</i>

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

$$
x =
\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{bmatrix}.
$$

---

## Dot Product

### Definition

Given $x, y \in \mathbb{R}^n$, the dot product is defined as:

$$
x^T y = \sum_{i=1}^{n} x_i y_i.
$$

---

### Intuition

---

The dot product measures similarity between two vectors:

- positive → same direction  
- zero → orthogonal  
- negative → opposite direction  

---

### Example

$$
x =
\begin{bmatrix}
1 \\
2 \\
4 \\
5
\end{bmatrix},
\quad
y =
\begin{bmatrix}
1 \\
3 \\
4 \\
-5
\end{bmatrix}
$$

$$
x^T y =
\begin{bmatrix}
1 & 2 & 4 & 5
\end{bmatrix}
\begin{bmatrix}
1 \\
3 \\
4 \\
-5
\end{bmatrix}
= -2.
$$

---

### Calculation

$$
1 \cdot 1 + 2 \cdot 3 + 4 \cdot 4 + 5 \cdot (-5)
= 1 + 6 + 16 - 25
= -2
$$

## Outer Product


### Definition

Given $x \in \mathbb{R}^m$ and $y \in \mathbb{R}^n$, the outer product is defined as:

$$
xy^T \in \mathbb{R}^{m \times n}
$$

with entries:

$$
(xy^T)_{ij} = x_i y_j.
$$
### Intuition

---

The outer product builds a matrix where each entry is the product of one component of $x$ and one component of $y$.
Each row is a scaled version of $y^T$.

---

### Example

$$
x =
\begin{bmatrix}
20 \\
32 \\
23
\end{bmatrix},
\quad
y =
\begin{bmatrix}
53 \\
28 \\
76
\end{bmatrix}
$$

$$
xy^T =
\begin{bmatrix}
20 \\
32 \\
23
\end{bmatrix}
\begin{bmatrix}
53 & 28 & 76
\end{bmatrix}
$$

$$
\begin{bmatrix}
20 \cdot 53 & 20 \cdot 28 & 20 \cdot 76 \\
32 \cdot 53 & 32 \cdot 28 & 32 \cdot 76 \\
23 \cdot 53 & 23 \cdot 28 & 23 \cdot 76
\end{bmatrix}=
\begin{bmatrix}
1060 & 560 & 1520 \\
1696 & 896 & 2432 \\
1219 & 644 & 1748
\end{bmatrix}.
$$
## Matrix-Vector Products

---

### Definition

Given a matrix $A \in \mathbb{R}^{m \times n}$ and a vector $x \in \mathbb{R}^n$, their product is a vector $y = Ax \in \mathbb{R}^m$.

$$
y = Ax =
\begin{bmatrix}
a_1^T \\
a_2^T \\
\vdots \\
a_m^T
\end{bmatrix}
x
=
\begin{bmatrix}
a_1^T x \\
a_2^T x \\
\vdots \\
a_m^T x
\end{bmatrix}.
$$

### Intuition

---

The matrix-vector product transforms a vector into another vector.
Each entry of the result is the dot product between one row of the matrix and the vector.

---
### Example

$$
A =
\begin{bmatrix}
1 & 2 & 4 \\
2 & 3 & 5 \\
3 & 10 & 8
\end{bmatrix},
\quad
x =
\begin{bmatrix}
3 \\
4 \\
4
\end{bmatrix}
$$


$$
y = Ax =
\begin{bmatrix}
27 \\
38 \\
81
\end{bmatrix}.
$$

---

### Calculation
$$
a_1^T x = 1 \cdot 3 + 2 \cdot 4 + 4 \cdot 4 = 27
$$
$$
a_2^T x = 2 \cdot 3 + 3 \cdot 4 + 5 \cdot 4 = 38
$$
$$
a_3^T x = 3 \cdot 3 + 10 \cdot 4 + 8 \cdot 4 = 81
$$

---
## Matrix-Matrix Products
## Definition
The product of two matrices is obtained by taking the dot product of each row of the first matrix with each column of the second matrix.
$$
C = AB=\begin{bmatrix}
— & a^T_1 & — \\
— & a^T_2 & — \\
& \vdots \\
— & a^T_m & — 
\end{bmatrix}
\begin{bmatrix}
| & | & &|\\
b_1 & b_2 &\dots & b_p \\
| & | & &|
\end{bmatrix}
=
\begin{bmatrix}
a_1^T b_1 & a_1^T b_2 & \cdots & a_1^T b_p \\
a_2^T b_1 & a_2^T b_2 & \cdots & a_2^T b_p \\
\vdots & \vdots & \ddots & \vdots \\
a_m^T b_1 & a_m^T b_2 & \cdots & a_m^T b_p
\end{bmatrix}.
$$
## Intiution
Each entry of the product matrix tells us how much a row of the first matrix aligns with a column of the second matrix.
So matrix multiplication combines rows and columns to produce new values that summarize their interactions.

---
## Example 
$$
A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix},
\qquad
B =
\begin{bmatrix}
5 & 6 \\
7 & 8
\end{bmatrix}
$$

$$
AB =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\begin{bmatrix}
5 & 6 \\
7 & 8
\end{bmatrix}
=
\begin{bmatrix}
1 \cdot 5 + 2 \cdot 7 & 1 \cdot 6 + 2 \cdot 8 \\
3 \cdot 5 + 4 \cdot 7 & 3 \cdot 6 + 4 \cdot 8
\end{bmatrix}
=
\begin{bmatrix}
19 & 22 \\
43 & 50
\end{bmatrix}.
$$
## Column and Row views

In the outer product formulation C = AB:

- $a_i$ → i-th **column** of $A$
- $b_i^T$ → i-th **row** of $B$ (= i-th column of $B$, transposed)

Same data, different orientation.

---
## Iterpretation

$$C = AB = 
\begin{bmatrix}
\mid &\mid&  \ &\mid\\ 
a^1 & a^2 &\cdots &a^n \\
\mid & \mid & &\mid
\end{bmatrix}
\begin{bmatrix}
— & b^T_1& — \\
— &b^T_1& —\\
&\vdots \\
— & b^T_n& —
\end{bmatrix}
= \sum^n_{i =1} a_ib_i^T .
$$
---
