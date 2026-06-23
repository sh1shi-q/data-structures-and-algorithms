#include <stdio.h>

int matrix[3][3] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}   
};

void print_matrix(int rows, int cols, int matrix[rows][cols]) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

void transpose(int rows, int cols, int matrix[rows][cols]) {
    int temp;
    for (int i = 0; i < rows; i++) {
        for (int j = i + 1; j < cols; j++) {
            temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }
}

void rotate_90(int rows, int cols, int matrix[rows][cols]) {
    transpose(rows, cols, matrix);
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols / 2; j++) {
            int temp = matrix[i][j];
            matrix[i][j] = matrix[i][cols - j - 1];
            matrix[i][cols - j - 1] = temp;
        }
    }
}

void rotate_180(int rows, int cols, int matrix[rows][cols]) {
    rotate_90(rows, cols, matrix);
    rotate_90(rows, cols, matrix);
}

void spiral_print(int rows, int cols, int matrix[rows][cols]) {
    int top = 0, bottom = rows - 1, left = 0, right = cols - 1;
    while (top <= bottom && left <= right) {
        for (int i = left; i <= right; i++) {
            printf("%d ", matrix[top][i]);
        }
        top++;
        for (int i = top; i <= bottom; i++) {
            printf("%d ", matrix[i][right]);
        }
        right--;
        if (top <= bottom) {
            for (int i = right; i >= left; i--) {
                printf("%d ", matrix[bottom][i]);
            }
            bottom--;
        }
        if (left <= right) {
            for (int i = bottom; i >= top; i--) {
                printf("%d ", matrix[i][left]);
            }
            left++;
        }
    }
}

void prefix_sum(int rows, int cols, int matrix[rows][cols], int prefix[rows][cols]) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            prefix[i][j] = matrix[i][j];
            if (i > 0) prefix[i][j] += prefix[i - 1][j];
            if (j > 0) prefix[i][j] += prefix[i][j - 1];
            if (i > 0 && j > 0) prefix[i][j] -= prefix[i - 1][j - 1];
        }
    }
}

int main() {
    int prefix[3][3];

    printf("Original Matrix:\n");
    print_matrix(3, 3, matrix);

    printf("\nPrefix Sum Matrix:\n");
    prefix_sum(3, 3, matrix, prefix);
    print_matrix(3, 3, prefix);

    printf("\nTransposed Matrix:\n");
    transpose(3, 3, matrix);
    print_matrix(3, 3, matrix);

    printf("\nRotated 90 Degrees:\n");
    rotate_90(3, 3, matrix);
    print_matrix(3, 3, matrix);

    printf("\nRotated 180 Degrees:\n");
    rotate_180(3, 3, matrix);
    print_matrix(3, 3, matrix);

    printf("\nSpiral Print:\n");
    spiral_print(3, 3, matrix);
    printf("\n");

    return 0;
}

