# Week 2 – Day 3: Matrix Multiplication (Deep & Detailed Guide)

## 1. Core Definition
Matrix multiplication is defined as **row-by-column dot products**.

If A is (m×n) and B is (n×p),  
then AB is (m×p).

**Rule:**  
(AB)[i,j] = sum over k of A[i,k] * B[k,j]

Inner dimensions must match.

---

## 2. Example (2×2 × 2×2)

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

Compute entries:

Row1·Col1 → 1*5 + 2*7 = 19  
Row1·Col2 → 1*6 + 2*8 = 22  
Row2·Col1 → 3*5 + 4*7 = 43  
Row2·Col2 → 3*6 + 4*8 = 50  

**Result:**
[[19, 22],  
 [43, 50]]

---

## 3. Why Matrix Multiplication Matters in ML

### Linear Regression
Normal equation uses:  
θ = (XᵀX)⁻¹ Xᵀy

### Neural Networks
Every layer performs:  
Wx + b  
which is matrix multiplication + addition.

### PCA
Covariance = XᵀX

### Transformers / Attention
Attention = softmax(QKᵀ)V

Matrix multiplication powers every part of ML.

---

## 4. Geometric Meaning

A matrix is a **linear transformation**.

Examples:

### Scaling
[2 0]  
[0 1]  
→ stretches x-axis by 2

### Rotation
[0 -1]  
[1  0]  
→ rotates vectors 90°

Matrix multiplication AB = applying transformation B first, then A.

This is how neural network layers stack transformations.

---

## 5. Shape Compatibility (Must Learn)

### Valid:
3×3 × 3×3 → 3×3  
3×2 × 2×5 → 3×5  
2×3 × 3×1 → 2×1  

### Invalid:
3×2 × 3×3 → inner dims mismatch (2 ≠ 3)

Shape discipline prevents 90% of ML bugs.

---

## 6. Visual / Mental Interpretation

- Think of matrix A as a machine that transforms vectors.
- Matrix B is another machine.
- AB means “run B first, then A.”
- Picture vectors being rotated, scaled, sheared, flipped.

---

## 7. Day 3 Mental Practice (Do quietly)

1. Visualize a 2×3 multiplied by a 3×1 → 2×1 output.  
2. Imagine rotation × scaling transformations.  
3. Imagine chaining two 2D transformations.  
4. Think of neural layers as stacked matrix multiplications.

---
