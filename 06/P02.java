// find the missing number in the array

import java.util.Scanner;

class P02 {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        System.out.print("\nenter array size ");
        int n = input.nextInt();
        System.out.print("enter array: ");
        int sum = 0;
        for (int i = 0; i < n; i++)
            sum += input.nextInt();
        int res = n * (n+1) / 2 - sum;
        System.out.println(res);
        System.out.println();
    }
}