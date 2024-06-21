# binary search tree
print()


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST_X:

    def sum_values(self):
        def sum(head):
            if head == None:
                return 0
            return head.val + sum(head.left) + sum(head.right)
        res = sum(self.head)
        print("sum =", res)

    def sum_even_values(self):
        def sum(head):
            if head == None:
                return 0
            if head.val % 2 != 0:
                return sum(head.left) + sum(head.right)
            return head.val + sum(head.left) + sum(head.right)
        print("even sum =", sum(self.head))

    def sum_odd_values(self):
        def sum(head):
            if head == None:
                return 0
            if head.val % 2 == 0:
                return sum(head.left) + sum(head.right)
            return head.val + sum(head.left) + sum(head.right)
        print("odd sum =", sum(self.head))

    def diff_sum_even_odd(self):
        def sum(head):
            if head == None:
                return 0
            if head.val % 2 == 0:
                return head.val + sum(head.left) + sum(head.right)
            else:
                return -head.val + sum(head.left) + sum(head.right)
        print("diff even odd sums =", abs(sum(self.head)))
    
    def height(self, head):
        if head == None:
            return -1
        return 1 + max(self.height(head.left), self.height(head.right))
    
    def balanced(self):
        def recur(head):
            if head == None:
                return True
            return abs(self.height(head.left) - self.height(head.right)) <= 1
        return recur(self.head)
    
    def no_of_leaf_nodes(self):
        def recur(head):
            if head == None:
                return 0
            if head.left == None and head.right == None:
                return 1
            return recur(head.left) + recur(head.right)
        return recur(self.head)
    
    def search_and_depth(self, val):
        def recur(val, head, depth):
            if head == None:
                return -1
            if val == head.val:
                return depth
            if val < head.val:
                return recur(val, head.left, depth+1)
            if val > head.val:
                return recur(val, head.right, depth+1)
        res = recur(val, self.head, 0)
        if res != -1:
            print(f"depth of node with value {val} =", res)
        else:
            print(f"node with value {val} not found")


class BST(BST_X):

    def __init__(self):
        self.head = None

    def add(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            x = self.head
            parent = self.head
            while x != None:
                parent = x
                if val < x.val:
                    x = x.left
                else:
                    x = x.right
            if val < parent.val:
                parent.left = Node(val)
            else:
                parent.right = Node(val)
    
    def traverse(self):
        def inorder(head):
            if head == None:
                return
            inorder(head.left)
            print(head.val, end=' ')
            inorder(head.right)
        print("inorder:", end=' ')
        inorder(self.head)
        print()
        def preorder(head):
            if head == None:
                return
            print(head.val, end=' ')
            preorder(head.left)
            preorder(head.right)
        print("preorder:", end=' ')
        preorder(self.head)
        print()
        def postorder(head):
            if head == None:
                return
            postorder(head.left)
            postorder(head.right)
            print(head.val, end=' ')
        print("postorder:", end=' ')
        postorder(self.head)
        print()
    
    

tree = BST()
tree.add(2)
tree.add(1)
tree.add(3)
tree.add(4)
tree.traverse()
tree.sum_values()
tree.sum_even_values()
tree.sum_odd_values()
tree.diff_sum_even_odd()
print("tree height =", tree.height(tree.head))
print("balanced =", tree.balanced())
print("no. of leaf nodes =", tree.no_of_leaf_nodes())
tree.search_and_depth(7)

print()