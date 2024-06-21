/*
explanation: each row should contain unique elements with as less lists as possible
*/

import java.util.Scanner;
import java.util.ArrayList;

class P00 {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        ArrayList<Integer> arr = new ArrayList<Integer>();
        for(int i = 0; i < n; i++)
            arr.add(input.nextInt());
        ArrayList<ArrayList<Integer>> list = new ArrayList<ArrayList<Integer>>();
        while (arr.size() > 0) {
            ArrayList<Integer> temp = new ArrayList<Integer>();
            for (int i = 0; i < arr.size(); i++)
                if (!temp.contains(arr.get(i)))
                    temp.add(arr.get(i));
            for (Integer i : temp)
                arr.remove(i);
            list.add(temp);
        }
        System.out.println(list);
    }
}