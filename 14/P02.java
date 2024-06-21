// coin change

import java.util.Scanner;
import java.util.Arrays;

class P02 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int[] coins = new int[n];
        for (int i = 0; i < n; i++)
            coins[i] = scanner.nextInt();
        Arrays.sort(coins);
        int amount = scanner.nextInt();

        int[] array = new int[amount+1];
        Arrays.fill(array, -1);
        array[0] = 0;

        for (int i : coins) {
            for (int j = i; j <= amount; j++)
                if (array[j-i] != -1)
                    if (array[j] != -1)
                        array[j] = Math.min(array[j], array[j-i] + 1);
                    else
                        array[j] = array[j-1] + 1;
        }

        System.out.println(array[amount]);
    }
}