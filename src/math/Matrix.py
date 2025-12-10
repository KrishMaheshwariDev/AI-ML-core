def matrix_add(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("matrix shape is not same, operation not possible")
        return
    c = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[i])):
            c[i][j] = a[i][j] + b[i][j]
    return c

def matrix_sub(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("matrix shape is not same, operation not possible")
        return
    c = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[i])):
            c[i][j] = a[i][j] - b[i][j]
    return c

def scalar_mul_matrix(s, a):
    c = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[i])):
            c[i][j] = s*a[i][j]
    return c

def matrix_vector_mul(A, V):
    if len(A[0]) != len(V):
        print("Dimensions do not match for matrix-vector multiplication")
        return
    result = [0 for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(V)):
            result[i] += A[i][j] * V[j]
    return result

def matrix_mul(A, B):
    if len(A[0]) != len(B):
        print("Matrix shapes incompatible for multiplication")
        return
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

A = [[2,3], [1, -1]]
V = [1, 0]

re = matrix_vector_mul(A, V)
print(re)

V = [0, 1]
re = matrix_vector_mul(A, V)
print(re)