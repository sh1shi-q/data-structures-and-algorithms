

public class Matrix {
    int[][] matrix = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    public void print() {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }

    public void transpose() {
        int[][] transposed = new int[matrix[0].length][matrix.length];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                transposed[j][i] = matrix[i][j];
            }
        }
        matrix = transposed;
    }

    public void rotateImage90Degrees() {
        transpose();
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length / 2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][matrix[i].length - 1 - j];
                matrix[i][matrix[i].length - 1 - j] = temp;
            }
        }
    }

    public void rotateImage180Degrees() {
        int rows = matrix.length;
        int cols = matrix[0].length;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                int ni = rows - 1 - i;
                int nj = cols - 1 - j;
                if (i > ni || (i == ni && j >= nj)) {
                    continue;
                }
                int temp = matrix[i][j];
                matrix[i][j] = matrix[ni][nj];
                matrix[ni][nj] = temp;
            }
        }
    }

    public void spiralPrint() {
        int top = 0;
        int bottom = matrix.length - 1;
        int left = 0;
        int right = matrix[0].length - 1;

        while (top <= bottom && left <= right) {
            for (int i = left; i <= right; i++) {
                System.out.print(matrix[top][i] + " ");
            }
            top++;

            for (int i = top; i <= bottom; i++) {
                System.out.print(matrix[i][right] + " ");
            }
            right--;

            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    System.out.print(matrix[bottom][i] + " ");
                }
                bottom--;
            }

            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    System.out.print(matrix[i][left] + " ");
                }
                left++;
            }
        }
    }

    public int[][] prefixSum() {
        int[][] prefSum = new int[matrix.length][matrix[0].length];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                prefSum[i][j] = matrix[i][j];
                if (i > 0) {
                    prefSum[i][j] += prefSum[i - 1][j];
                }
                if (j > 0) {
                    prefSum[i][j] += prefSum[i][j - 1];
                }
                if (i > 0 && j > 0) {
                    prefSum[i][j] -= prefSum[i - 1][j - 1];
                }
            }
        }
        return prefSum;
    }

    public static void main(String[] args) {
        Matrix m = new Matrix();
        m.print();

        System.out.print("\nSpiral Print: ");
        m.spiralPrint();

        System.out.println("\n\nTransposed Matrix:");
        m.transpose();
        m.print();

        System.out.println("\nPrefix Sum Matrix:");
        int[][] prefixSum = m.prefixSum();
        for (int i = 0; i < prefixSum.length; i++) {
            for (int j = 0; j < prefixSum[i].length; j++) {
                System.out.print(prefixSum[i][j] + " ");
            }
            System.out.println();
        }

        m.rotateImage90Degrees();
        System.out.println("\n90-Degree Rotated Matrix:");
        m.print();
        
        Matrix m2 = new Matrix();
        m2.rotateImage180Degrees();
        System.out.println("\n180-Degree Rotated Matrix:");
        m2.print();


    }
}