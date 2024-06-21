// number of paths from start to end in a grid
// can move up, left, down, right

import java.util.Scanner;

class P04 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int x = scanner.nextInt();
        int y = scanner.nextInt();
        int[][] grid = new int[x+1][y+1];
        for (int i = 0; i <= x; i++)
            for (int j = 0; j <= y; j++)
                grid[i][j] = 0;
        grid[1][1] = 1;
        
        for (int i = 1; i <= x; i++)
            for (int j = 1; j <= y; j++)
                grid[i][j] += grid[i-1][j-1] + grid[i-1][j] + grid[i][j-1];
        
        System.out.println(grid[x][y]);
    }
}