// return all possible combinations of length 3

import java.util.Scanner;
import java.util.ArrayList;

class P00 {
    public static void combinations(int[] nums, int index, ArrayList<Integer> list) {
        if (index == nums.length)
            return;
        if (list.size() == 3) {
            System.out.println(list);
            return;
        }
        list.add(nums[index]);
        for (int i = list.size(); i < nums.length; i++) {
            combinations(nums, i, list);
            list.remove(Integer.valueOf(nums[index]));
        }
    }
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        if (n < 3)
            return;
        int[] nums = new int[n];
        for (int i = 0; i < n; i++)
            nums[i] = input.nextInt();
        ArrayList<Integer> list = new ArrayList<Integer>();
        combinations(nums, 0, list);
    }
}