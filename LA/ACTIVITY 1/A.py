# MATRIX CREATION

rows = 3
cols = 3

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i * cols + j + 1)
    matrix.append(row)

print(matrix)
