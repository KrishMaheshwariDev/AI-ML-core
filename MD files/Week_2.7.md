# Week 2 – Day 7: Integration of Linear Algebra into ML Data Flow

## 1. The ML Data Matrix (X)

In machine learning, data is always represented as:

X ∈ ℝ^(m × n)

- m = number of samples (rows)
- n = number of features (columns)

Each sample is a **row vector**.  
Each feature is a **column vector**.

This structure lets us use matrix operations to process entire datasets efficiently.

---

## 2. Predictions as Matrix Multiplication

A linear model predicts using:

ŷ = XW

Where:
- X is m×n
- W is n×1
- ŷ is m×1 (one prediction per sample)

Your `matrix_mul` and `matrix_vector_mul` directly implement this behavior.

---

## 3. Loss Computation Using Vector Operations

Loss functions use vector arithmetic:

### L2 Loss
L = ||ŷ − y||₂²  
Uses:
- vector_sub
- dot or l2_norm

### L1 Loss
L = ||ŷ − y||₁  
Uses:
- vector_sub
- l1_norm

These operations form the basis of optimization and training.

---

## 4. Gradient Descent as a Linear Transformation Process

A gradient update:

W_new = W_old − α * gradient

is purely vector math:

- subtraction
- scalar multiplication
- dot products
- matrix-vector multiplication for prediction

Every step in gradient descent corresponds to a geometric transformation in weight space.

---

## 5. The Importance of Shapes

Machine learning code breaks primarily due to shape mismatches:

- X (m×n) must match W (n×1)
- prediction outputs must match y
- multiplication order must be consistent

Your added shape checks make your linear algebra stable and ML-safe.

---

## 6. Determinants, Inverses & ML Stability

### Determinant
det ≠ 0 → matrix is invertible  
det = 0 → singular; dimension collapsed

### ML meaning:
- normal equation solution (XᵀX)⁻¹ may not exist if det = 0  
- PCA requires full-rank covariance  
- optimization stability depends on curvature (Hessian determinant)

You now understand how invertibility and rank impact model solvability.

---

## 7. Mental Integration Exercise

You completed:
1. Imagining a dataset X (3×2)
2. A weight vector W (2×1)
3. Computing predictions: Y = XW
4. Computing error: Y − y
5. Computing loss via vector norms
6. Imagining gradient-based weight updates

This mental model maps exactly to how real ML frameworks operate internally.

---

## Summary
You now understand the complete flow:

Data → Matrix Form  
Weights → Vector Form  
Prediction → Multiplication  
Loss → Vector Norms  
Optimization → Linear Transformations  
Stability → Determinants & Inverses  

Week 2 gives you the mathematical backbone required for Week 3.
