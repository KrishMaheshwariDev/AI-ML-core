# Week 2 – Day 5: Determinants & Inverses (Structure, Solvability, PCA Core)

## 1. Determinant — What It Really Measures
The determinant measures **how much a matrix scales space**.

For a 2×2 matrix, det tells you:
- how area changes after transformation
- whether orientation flips
- whether the matrix collapses space (det = 0)

### Geometric meaning:
Apply matrix A to the unit square → it becomes a parallelogram.  
**Area of that parallelogram = det(A).**

- det > 0 → area preserved in orientation  
- det < 0 → area preserved but flipped  
- det = 0 → collapsed dimension → no inverse possible

This determines:
- whether equations have unique solutions  
- whether PCA works  
- whether regression is solvable  

---

## 2. Determinant Formula (2×2)

For:
```
[a b]
[c d]
```

The determinant is: ad − bc

### Example:
```
[1 2]
[3 4]
```

det = 1x4 − 2x3 = −2

---

## 3. When det = 0 (Singularity)
det = 0 means the matrix:
- collapses 2D space into a line  
- loses information  
- has linearly dependent rows/columns  
- is **not invertible**

### ML failures when det = 0:
- regressions via (XᵀX)⁻¹ fail  
- covariance matrices lose dimensions  
- PCA cannot compute components  
- solutions become infinite or undefined

---

## 4. Matrix Inverse — What It Actually Means
A⁻¹ is the matrix that **undoes** A.

Definition:
A⁻¹ A = I

yaml
Copy code

Interpretation:
- A transforms space
- A⁻¹ reverses that transformation

Only matrices with **det ≠ 0** have inverses.

---

## 5. Formula for 2×2 Inverse

For:
```
[a b]
[c d]
```

The inverse is:
```
1/(ad − bc) * [d -b] 
              [-c a]
```

Denominator contains det(A).  
If det = 0 → inverse impossible.

Small determinants → unstable, explodes values → numerical instability in ML.

---

## 6. Geometric Meaning of Inverse
If A:
- rotates 90°
- scales x by 2
- shears right by 1

Then A⁻¹:
- rotates -90°
- scales x by 1/2
- shears left by -1

Inverse reverses the transformation exactly.

---

## 7. ML Connections

### Linear Regression
Normal equation:
θ = (XᵀX)⁻¹ Xᵀ y

yaml
Copy code
Requires (XᵀX) invertible.

### PCA
Covariance matrix must be full-rank → det ≠ 0.

### Optimization
Hessian determinant tells:
- minima  
- maxima  
- saddle points

### Stability
Small det → A⁻¹ unstable → gradients blow up.

---

## 8. Mental Practice (Quiet Work)
- Compute det using ad − bc for any 2×2 matrix in your mind.
- Visualize the unit square becoming a parallelogram.
- Imagine det = 0 → collapse to a line.
- Picture A and A⁻¹ undoing each other’s transformations.

---