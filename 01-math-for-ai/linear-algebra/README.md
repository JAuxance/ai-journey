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
\end{bmatrix}
$$

---

## Dot Product

### Definition

Given $x, y \in \mathbb{R}^n$, the dot product is defined as:

$$
x^T y = \sum_{i=1}^{n} x_i y_i
$$

---

### Intuition

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
= -2
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
(xy^T)_{ij} = x_i y_j
$$
### Intuition

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
\end{bmatrix}
$$
## Matrix-Vector Products
### Definition

Given a matrix $A$ $\in\mathbb{R}^{m\times n}$ and a vector $x$ $\in\mathbb{R}^n$, thier poduct is a vector $y= Ax \in^m$.

$$y = Ax = \begin{bmatrix}— & a^T_1&— \\
— & a^T_2 &— \\
& \vdots\\
— &a^T_m &—
\end{bmatrix}
x =
\begin{bmatrix}a^T_1x\\
a^T_2x\\
\vdots\\
a^T_mx\end{bmatrix}
$$
---

### Example

$$A = \begin{bmatrix}1 & 2 & 4\\ 2 & 3 & 5\\ 3 & 10 & 8\end{bmatrix}, \quad
x = \begin{bmatrix}3 \\ 4 \\ 4\end{bmatrix}$$

$$y = Ax = \begin{bmatrix}27 \\ 38 \\ 81\end{bmatrix}$$
---
### Calculation
$$A_{1,:} \cdot x = 1\cdot 3 + 2\cdot 4 + 4\cdot 4 = 27$$
$$A_{2,:} \cdot x = 2\cdot 3 + 3\cdot 4 + 5\cdot 4 = 38$$
$$A_{3,:} \cdot x = 3\cdot 3 + 10\cdot 4 + 8\cdot 4 = 81$$
