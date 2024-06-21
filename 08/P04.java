/*
4
tued
fwow
roer
frui
word
constraint: move 4 sides, check if word can be formed or not
*/

import java.util.Scanner;

class P04 {
    static boolean checkword(String[] strings, String word, int index, int i, int j) {
        if (i < 0 || i == strings.length || j < 0 || j == strings[0].length() || index == word.length())
            return false;
        if (index == (word.length-1) && strings[i][j] == word[index])
            return true;
        boolean b = 
    }
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        String[] strings = new String[n];
        for (int i = 0; i < n; i++)
            strings[i] = input.next();
        String word = input.next();
        boolean present = false;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < strings[i].length; j++) {
                if (strings[i].charAt(j) == word.charAt(0)) {
                    present = present || checkword(strings, word, 0, i, j);
                }
            }
        }
    }
}