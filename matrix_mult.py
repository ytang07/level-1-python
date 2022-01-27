mat_a = [[1, 2, 3, 4],
         [2, 4, 1, 3],
         [4, 2, 3, 1],
         [3, 1, 4, 2]]

mat_b = [[4, 2, 1, 3],
         [3, 4, 1, 2],
         [1, 2, 4, 3],
         [2, 1, 3, 4]]

# expected result:
# [[21, 20, 27, 32],
#  [27, 25, 19, 29],
#  [27, 23, 21, 29],
#  [23, 20, 26, 31]]

mat_c = [[1, 2],
         [2, 1]]

mat_d = [[3, 4],
         [4, 3]]

# expected result:
# [[11, 10],
#  [10, 11]]

def validate(mat_a, mat_b):
    len_a = len(mat_a)
    len_b = len(mat_b[0])
    assert len_a == len_b

def mat_mul(mat_a, mat_b):
    validate(mat_a, mat_b)
    # turn matrix b into a list of tuples
    iterable_b = list(zip(*mat_b))
    return [[sum(a*b for a, b in zip(row_a, col_b)) for col_b in iterable_b] for row_a in mat_a]

print(mat_mul(mat_a, mat_b))
print(mat_mul(mat_c, mat_d))