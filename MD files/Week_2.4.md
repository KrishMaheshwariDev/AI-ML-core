# Week 2 – Day 4: Linear Transformations (Geometry of ML)

## 1. What a Linear Transformation Really Is
A linear transformation T satisfies:
- T(ax) = a·T(x)
- T(x + y) = T(x) + T(y)

A matrix represents such a transformation.  
It does not transform just one vector — it transforms the **entire coordinate system**.

---

## 2. How a Matrix Transforms Space
Each matrix:
- moves the x-axis to a new direction,
- moves the y-axis to a new direction,
- and every vector follows this movement.

A matrix reshapes the whole space.

---

## 3. The Four Fundamental 2D Transformations

### (A) Scaling
``` 
[ sx 0 ]
[ 0 sy ] 
```

Example:
```
[2 0]
[0 1]
```
→ stretches x-axis by 2.

**ML Meaning:**  
Feature amplification, normalization, weight scaling.

---

### (B) Rotation
```
[ cosθ -sinθ ]
[ sinθ cosθ ]
```
Example (90°):
```
[0 -1]
[1 0]
```
**ML Meaning:**  
Basis changes, PCA rotations, embedding transformations.

---

### (C) Shear
```
[1 k]
[0 1]
```
Example:
```
[1 1]
[0 1]
```

**ML Meaning:**  
Feature mixing; neural layers often behave like learned shear operators.

---

### (D) Reflection

```
[-1 0]
[ 0 1]
```

**ML Meaning:**  
Appears when transformations include flips or sign inversions.

---

## 4. Transforming Basis Vectors
To understand any matrix, see where it sends:
- (1, 0) → becomes **column 1**  
- (0, 1) → becomes **column 2**

These two vectors define the entire transformation.

---

## 5. Matrix Multiplication = Chaining Transformations
If C = A × B:
- apply **B first**
- then **A**

This is how neural networks apply layers:
x → W₁x → W₂(W₁x) → ...

Each W is a geometric transformation.

---

## 6. Visual Intuition

### Scaling
Squares → rectangles.

### Shear
Squares → parallelograms.

### Rotation
Grid rotates around origin.

### Reflection
Grid flips across an axis.

**Every ML algorithm reshapes space using these primitives.**

---

## 7. Example Transformations

### Scaling example
```
A = [2 0]
    [0 1]

A * [1,1]ᵀ = [2,1]ᵀ
```

### Rotation example

```
R = [0 -1]
    [1 0]

R * [1,0]ᵀ = [0,1]
R * [0,1]ᵀ = [-1,0]
```

### Shear example

```
S = [1 1]
    [0 1]

S * [1,1]ᵀ = [2,1]
```

---

## 8. ML Relevance
Linear transformations power:
- neural network layers (Wx)
- attention matrices (QKᵀ)
- PCA (rotation of basis)
- whitening
- covariance matrices
- dimensionality reduction
- optimization updates

Linear algebra *is* the geometry of ML.

---

## 9. Day 4 Mental Practice
- Apply scaling, rotation, shear to vector (1,1).
- Imagine where (1,0) and (0,1) move under random matrices.
- Think how a layer reshapes space.
- Mentally chain two transformations (order matters).

---