// 3 pointer decoy sorting
// sort each group of 3 consecutive elements
/*
    8                                                                                             
    4 9 8 2 14 3 5 6
    4 8 9
      2 8 9
        8 9 14
          3 9 14
            5 9 14
              6 9 14
    4 2 8 3 5 6 9 14
*/

import java.util.Scanner;

class P01 {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = input.nextInt();
        for (int i = 0; i < (n-2); i++) {
            int min1 = Math.min(Math.min(arr[i], arr[i+1]), arr[i+2]);
            int min3 = Math.max(Math.max(arr[i], arr[i+1]), arr[i+2]);
            int min2 = (arr[i] + arr[i+1] + arr[i+2]) - min1- min3;
            arr[i] = min1;
            arr[i+1] = min2;
            arr[i+2] = min3;
        }
        for (int i = 0; i < n; i++)
            System.out.print(arr[i] + " ");
    }
}