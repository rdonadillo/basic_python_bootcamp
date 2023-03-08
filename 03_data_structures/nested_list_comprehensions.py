# List Comprehensions

# Matrix Transposition -> Switching its rows with its columns
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]

transpose = []
for i in range(4):
    transpose_row = []
    
    for row in matrix:
        # print(row[i])
        transpose_row.append(row[i])

    transpose.append(transpose_row)

print(transpose)

# Same as
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]

transpose = []
for i in range(4):
    transpose.append([row[i] for row in matrix])

print(transpose)

# Same as
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]

transpose = [[row[i] for row in matrix] for i in range(4)]
print(transpose)


# Use numpy
import numpy as np
matrix = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
print(matrix.transpose())
