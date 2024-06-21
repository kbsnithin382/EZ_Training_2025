/*
6
0 1 1 1 0 1
0 1 0 0 1 0
1 0 0 1 0 0
0 0 0 1 1 1
1 1 0 0 0 1
1 1 1 0 0 0
3 5 => start location of tree fire
*/

import java.util.Scanner;

class P03 {
    static void burn(int[][] matrix, int i, int j) {
    if (i < 0 || i >= matrix.length || j < 0 || j >= matrix[0].length || matrix[i][j] == 0)
            return;
        matrix[i][j] = 0;
        burn(matrix, i-1, j);
        burn(matrix, i+1, j);
        burn(matrix, i, j-1);
        burn(matrix, i, j+1);
    }
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int[][] matrix = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                matrix[i][j] = input.nextInt();
        int row = input.nextInt();
        int col = input.nextInt();
        int unburned = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (matrix[i][j] == 1)
                    unburned++;
        System.out.println("\nunburned trees before wildfire = " + unburned);
        burn(matrix, row, col);
        unburned = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (matrix[i][j] == 1)
                    unburned++;
        System.out.println("unburned trees after wildfire = " + unburned + "\n");
    }
}

