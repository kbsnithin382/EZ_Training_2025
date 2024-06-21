// sum of largest primes between each pair of elements in the array
/*
    6
    4 8 14 22 36 68
    op: 137
*/

import java.util.Scanner;

class P00 {
    static boolean prime(int num) {
        if (num <= 1)
            return false;
        int end = (int)Math.sqrt(num);
        for (int i = 2; i <= end; i++)
            if (num % i == 0)
                return false;
        return true;
    }
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = input.nextInt();
        int sum = 0;
        for (int i = 1; i < n; i++) {
            int temp = arr[i] - 1;
            while (temp > arr[i-1]) {
                if (prime(temp)) {
                    sum += temp;
                    break;
                }
                temp--;
            }
        }
        System.out.println(sum);
    }
}