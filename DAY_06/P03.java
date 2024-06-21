// kth largest factor

import java.util.Scanner;

class P03 {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int k = input.nextInt();
        for (int i = n; i >= 1; i--) {
            if (n % i == 0) {
                if (k == 1) {
                    System.out.println(i);
                    break;
                }
                k--;
            }
        }
    }
}