# Week 2 – Day 2: Matrix Addition, Subtraction & Scalar Multiplication (Detailed Guide)

## 1. Matrix Addition (Elementwise Operation)

**Definition:** Two matrices can be added only if they have the same shape.  
**Rule:** (A + B)[i,j] = A[i,j] + B[i,j]

### Intuition
Adding two matrices shifts every data point by corresponding feature values.

### ML Usage
- Adding bias terms in linear models and neural networks
- Combining gradients from multiple mini-batches
- Adjusting datasets during normalization

### Example
[1  2]   +   [10 20]   =   [11 22]  
[3  4]       [30 40]       [33 44]

---

## 2. Matrix Subtraction

**Definition:** Elementwise difference of matrices with equal shape.  
**Rule:** (A − B)[i,j] = A[i,j] − B[i,j]

### ML Usage
- Gradient descent update step: W_new = W_old − α * dW
- Error calculations (prediction − target)

### Example
[5 10] − [2 3] = [3 7]

---

## 3. Scalar Multiplication

**Definition:** Multiply every element of the matrix by a scalar constant.  
**Rule:** (kA)[i,j] = k * A[i,j]

### ML Usage
- Learning rate scaling
- Regularization (L1/L2 shrinkage)
- Scaling entire datasets

### Geometry Effects
- k > 1 → expands/stretch space  
- 0 < k < 1 → compresses/shrinks space  
- k < 0 → flips direction + scales magnitude  

### Example
0.5 * [4 6] = [2 3]

---

## 4. Visual & Geometric Interpretation

- Matrix addition = translating vectors uniformly in feature space  
- Scalar multiplication = stretching or shrinking the dataset  
- Imagine shifting all points (addition) or zooming in/out (scaling)

---

## 5. Shape Compatibility (Critical for ML)

- Addition/Subtraction require identical shapes  
- Scalar multiplication always valid  

### Examples
- 3×3 + 3×3 → valid  
- 3×2 + 3×2 → valid  
- 3×2 + 2×3 → invalid  

---

## 6. Day 2 Practice (Mental)

- Create 3 pairs of matrices and check addition validity  
- Visualize matrix translation and scaling  
- Reinforce shape discipline before Day 3  
