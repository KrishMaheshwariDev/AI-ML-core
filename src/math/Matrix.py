def matrix_add(a, b):
    c = [[0 for _ in range(len(a))] for _ in range(len(b))]
    for i in range(0, a.__len__()):
        for j in range(0, a[i].__len__()):
            c[i][j] = a[i][j] + b[i][j]
    return c

def matrix_sub(a, b):
    c = [[0 for _ in range(len(a))] for _ in range(len(b))]
    for i in range(0, a.__len__()):
        for j in range(0, a[i].__len__()):
            c[i][j] = a[i][j] - b[i][j]
    return c

def scalar_mul_matrix(s, a):
    c = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]
    for i in range(0, a.__len__()):
        for j in range(0, a[i].__len__()):
            c[i][j] = s*a[i][j]
    return c

def matrix_vector_mul(A, V):
    result = [0 for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(V)):
            result[i] += A[i][j] * V[j]
    return result

def matrix_mul(A, B):
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