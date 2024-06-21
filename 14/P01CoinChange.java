// coin change

import java.util.Scanner;
import java.util.Arrays;

class P01CoinChange {
    public static void main(String[] args)  {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] coins = new int[n];
        for (int i = 0; i < n; i++)
            coins[i] = scanner.nextInt();
        int amount = scanner.nextInt();
        Arrays.sort(coins);
        int[][] table = new int[n+1][amount+1];
        for (int i = 0; i <= n; i++)
            for (int j = 0; j <= n; j++)
                table[i][j] = Integer.MAX_VALUE;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= amount; j++) {
                if (amount >= coins[i-1]) {
                    table[i][j] = Math.min(table[i-1][j], 1+table[i][amount-coins[i-1]]);
                }
                else
                    table[i][j] = table[i-1][j];
            }
        }
        System.out.println(table[n][amount]);
    }
}