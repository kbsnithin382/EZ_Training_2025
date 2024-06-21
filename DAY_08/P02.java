// length of longest substring without repeating characters (sliding window)

import java.util.Scanner;
import java.util.HashSet;

class P02 {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        String s = input.next();
        int n = s.length();
        HashSet<Character> map = new HashSet<Character>();
        int maxCount = 0;
        int i = 0;
        for (int j = 0; j < n; j++) {
            if (map.contains(s.charAt(j))) {
                while (s.charAt(i) != s.charAt(j))
                    map.remove(s.charAt(i++));
                map.remove(s.charAt(i++));
            }
            map.add(s.charAt(j));
            maxCount = Math.max(maxCount, j - i + 1);
        }
        System.out.println(maxCount);
    }
}