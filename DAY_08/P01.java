// check if all alphabets present in the string

import java.util.Scanner;
import java.util.HashSet;

class P01 {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        String s = input.nextLine();
        HashSet<Character> set = new HashSet<Character>();
        int n = s.length();
        for (int i = 0; i < n; i++)
            if (s.charAt(i) >= 97 && s.charAt(i) <= 122)
                set.add(s.charAt(i));
        System.out.println(set.size() == 26);
    }
}