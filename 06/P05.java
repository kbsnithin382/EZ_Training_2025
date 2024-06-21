// valid parentheses

import java.util.Scanner;
import java.util.Stack;

class P05 {
    public static i validParantheses(String s) {
        char[] str = s.toCharArray();
        Stack<Character> stack = new Stack<Character>();
        for (char c : str) {
            if (c == '(' || c == '{' || c == '[')
                stack.push(c);
            else if (!stack.isEmpty()) {
                char ch = stack.pop();
                if (!((ch == '(' && c == ')') || (ch == '{' && c == '}') || (ch == '[' && c == ']')))
                return false;
            }
            else
                return false;
        }
        if (!stack.isEmpty())
            return false;
        return true;
    }
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        String s = input.next();
        
    }
}