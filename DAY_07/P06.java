// binary search tree

import java.util.Scanner;

class Node {
    int val;
    Node left = null;
    Node right = null;
    Node() {
        this.val = 0;
    }
    Node(int val) {
        this.val = val;
    }
}

class BinarySearchTree {
    Node head = null;
    void add(int val) {
        if (head == null) {
            head = new Node(val);
            return;
        }
        Node temp = head;
        Node prev = null;
        while (temp != null) {
            prev = temp;
            if (val < temp.val)
                temp = temp.left;
            else
                temp = temp.right;
        }
        if (prev.val > val)
            prev.left = new Node(val);
        else
            prev.right = new Node(val);
    }
    void inorderTraversal(Node x) {
        if (x == null)
            return;
        inorderTraversal(x.left);
        System.out.print(x.val + " ");
        inorderTraversal(x.right);
    }
}

public class P06 {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        BinarySearchTree tree = new BinarySearchTree();
        int n = input.nextInt();
        while (n > 0) {
            int x = input.nextInt();
            tree.add(x);
            n--;
        }
        tree.inorderTraversal(tree.head);
    }
}