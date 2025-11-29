import math

def vector_add(x, y):
    if(len(x) != len(y)):
        print("Length of both vector is different, operation not possible")
        return
    c = []
    for i in range(len(x)):
        c.append(x[i] + y[i])
    return c

def vector_sub(x, y):
    if(len(x) != len(y)):
        print("Length of both vector is different, operation not possible")
        return
    c = []
    for i in range(len(x)):
        c.append(x[i] - y[i])
    return c

def scalar_mul_vector(s, a):
    c = [0 for _ in range(len(a))]
    for i in range(len(a)):
        c[i] = s * a[i]
    return c

def dot(a, b):
    if(len(a) != len(b)):
        print("Length of both vector is different, operation not possible")
        return
    r = 0
    for i in range(len(a)):
        r += a[i]*b[i]
    return r

def l1_norm(a):
    b = 0
    for i in range(len(a)):
        b += abs(a[i])
    return b

def l2_norm(a):
    b = 0
    for i in range(len(a)):
        b += pow(a[i],2)
    return math.sqrt(b)

# a = [10, 20]
# b = [15, 25]
# c = vector_add(a, b)
# print(c)