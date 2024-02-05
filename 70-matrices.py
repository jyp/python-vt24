

# a matrix is a list of lists
# Aᵢⱼ is going to be A[i][j]
# A is a list lists
# A[i] is a vector; the ith row of A.

# example:

A = [[1,2,7],
     [4,3,6]]

def zero_vector(n):
    return [0] * n

# zero matrix
def zero_with_sharing(m,n):
    return [zero_vector(n)] * m  # sharing can be surprising!

def zero_without_sharing(m,n):
    result = []
    for i in range(0,m):
        row = zero_vector(n)
        result.append(row)
    return result

def identity_variant1(n):
    # result = zero(n,n)
    result = []
    for i in range(0,n):
        row = zero_vector(n)
        row[i] = 1
        result.append(row)
    return result

def identity_WRONG(n):
    result = zero_with_sharing(n,n)
    for i in range(0,n):
        result[i][i] = 1 # modifying data is dangerous!
    return result

def identity(n):
    result = zero_without_sharing(n,n)
    for i in range(0,n):
        result[i][i] = 1 # modifying data is dangerous!
    return result


# print(identity(10))

def add_vector(u,v):
    assert len(u) == len(v)
    t = []
    for i in range(0,len(u)) :
        t.append(u[i] + v[i])
    return t

# print(add_vector([1,2,3],[4,5,6]))

def add(A,B):
    assert len(A) == len(B)
    C = []
    for i in range(0,len(A)) :
        C.append(add_vector(A[i], B[i]))
    return C

# print(add([[1,2,3], [0,0,0]], [[4,5,6]]))

def transpose(A):
    # transpose(A)[i][j] = A[j][i]
    # row0[j] = A[j][0]
    assert len(A) > 0
    result = []
    for i in range(0,len(A[0])):
        row = []
        for j in range(0,len(A)):
            row.append(A[j][i])
        result.append(row)
    return result

# print(transpose([[1,2,3],[4,5,6]]))
