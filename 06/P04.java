// check if 2 numbers are co-prime

import java.util.Scanner;

class P04 {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();
        int y = input.nextInt();
        int small = Math.min(x, y) / 2;
        boolean coprimes = true;
        for (int i = 2; i <= small; i++)
            if ((x % i == 0) && (y % i == 0)) {
                coprimes = false;
                System.out.println("not co-primes");
                break;
            }
        if (coprimes)
            System.out.println("co-primes");
    }
}