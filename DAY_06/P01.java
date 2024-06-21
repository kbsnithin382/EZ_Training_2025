// program to find the number that occurs more than n/2 times
// the input contains atleast one element like that

import java.util.Scanner;

class P01 {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        System.out.print("\nenter array size ");
        int n = input.nextInt();
        int[] arr = new int[n];
        System.out.print("enter array: ");
        for (int i = 0; i < n; i++)
            arr[i] = input.nextInt();
        int candidate = 0;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (count == 0)
                candidate = arr[i];
            if (candidate == arr[i])
                count++;
            else if (candidate != arr[i])
                count--;
        }
        System.out.println("\nmajority element is " + candidate);
        System.out.println();
    }
}