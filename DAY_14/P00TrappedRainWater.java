// trapped rain water (LeetCode)

import java.util.Scanner;

class P00TrappedRainWater {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int[] heights = new int[n];
        for (int i = 0; i < n; i++)
            heights[i] = scanner.nextInt();

        int[] right = new int[n];
        right[n-1] = heights[n-1];
        for (int i = n-2; i >= 0; i--)
            right[i] = Math.max(right[i+1], heights[i]);

        int left = heights[0];
        int trapped = 0;
        for (int i = 1; i < n-1; i++) {
            int water = Math.min(left, right[i+1]) - heights[i];
            if (water > 0)
                trapped += water;
            left = Math.max(left, heights[i]);
        }

        System.out.println(trapped);
    }
}
