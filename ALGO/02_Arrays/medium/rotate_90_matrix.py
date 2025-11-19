def rotate_matrix(matrix):
    n = len(matrix )
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix 
    
matrix = [[5, 4, 2, 0], [6, 5, 0, 1], [7, 0, 3, 1], [0, 5, 1, 2]]
print(rotate_matrix(matrix))