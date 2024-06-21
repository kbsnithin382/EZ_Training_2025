// find the nth fibanacci number

import java.util.Scanner;

class P01Fibanacci {
    static int fib(int n) {
        if (n == 0 || n == 1)
            return n;
        return fib(n-1) + fib(n-2);
    }
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner input = new Scanner(System.in);
        System.out.println(fib(input.nextInt()));
    }
}