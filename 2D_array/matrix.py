matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def print_matrix(matrix) -> None:
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()

def transpose(matrix) -> list:
    rows = len(matrix)
    cols = len(matrix[0]) 
    transposed = [[0] * rows for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed

    # return (list(row) for row in zip(*matrix))

def rotate_90(matrix) -> list:
    return [list(reversed(col)) for col in zip(*matrix)]

def rotate_180(matrix) -> list:
    return [list(reversed(row)) for row in reversed(matrix)]

def spiral_order(matrix) -> list:
    result = []
    while matrix:
        result += matrix.pop(0) 
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop()) 
        if matrix:
            result += matrix.pop()[::-1] 
        if matrix and matrix[0]:
            for row in reversed(matrix):
                result.append(row.pop(0)) 
    return result

def prefix_sum(matrix) -> list:
    rows = len(matrix)
    cols = len(matrix[0]) 
    prefix = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            prefix[i][j] = matrix[i][j]
            if i > 0:
                prefix[i][j] += prefix[i - 1][j]
            if j > 0:
                prefix[i][j] += prefix[i][j - 1]
            if i > 0 and j > 0:
                prefix[i][j] -= prefix[i - 1][j - 1]
    return prefix

if __name__ == "__main__":
    print("Original Matrix:")
    print_matrix(matrix)

    print("\nTransposed Matrix:")
    transposed = transpose(matrix)
    print_matrix(transposed)

    print("\n90 Degree Rotation:")
    rotated_90 = rotate_90(matrix)
    print_matrix(rotated_90)

    print("\n180 Degree Rotation:")
    rotated_180 = rotate_180(matrix)
    print_matrix(rotated_180)

    print("\nPrefix Sum Matrix:")
    prefix = prefix_sum(matrix)
    print_matrix(prefix)
    
    print("\nSpiral Order:")
    spiral = spiral_order(matrix)
    print(spiral)
    

    