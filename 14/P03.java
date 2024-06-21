// paths to traverse a grid

import java.util.Scanner;

class P03 {
    static int paths(int i, int j, int m, int n, int a, int b) {
        if (i == m - 1 && j == n - 1)
            return 1;
        if (i == m - 1)
            return paths(i, j+1, m, n, a, b);
        if (j == n - 1)
            return paths(i+1, j, m, n, a, b);

        if (i == a && i == b)
            return 0;
        if (i == a)
            return paths(i, j+1, m, n, a, b);
        if (j == b)
            return paths(i+1, j, m, n, a, b);

        int x = paths(i+1, j, m, n, a, b);
        x += paths(i, j+1, m, n, a, b);
        return x;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int m = scanner.nextInt();
        int n = scanner.nextInt();
        
        int a = scanner.nextInt();
        int b = scanner.nextInt();

        System.out.println(paths(0, 0, m, n, a, b));
    }
}