# top, right, bottom, left views of a binary tree using recursion

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def add(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            def recur(root, val):
                if val < root.val:
                    if root.left == None:
                        root.left = Node(val)
                        return
                    recur(root.left, val)
                if val > root.val:
                    if root.right == None:
                        root.right = Node(val)
                        return
                    recur(root.right, val)
            recur(self.root, val)
    def traverse(self):
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            print(root.val, end=' ')
            inorder(root.right)
        def preorder(root):
            if root == None:
                return
            print(root.val, end=' ')
            preorder(root.left)
            preorder(root.right)
        def postorder(root):
            if root == None:
                return
            postorder(root.left)
            postorder(root.right)
            print(root.val, end=' ')
        print("inorder:", end=' ')
        inorder(self.root)
        print()
        print("preorder:", end=' ')
        preorder(self.root)
        print()
        print("postorder:", end=' ')
        postorder(self.root)
        print()
    def top_view(self):
        def recur(root, v, dic):
            if root == None:
                return
            recur(root.left, v-1, dic)
            recur(root.right, v+1, dic)
            dic[v] = root.val
        dic = {}
        recur(self.root, 0, dic)
        print("top view:", end=' ')
        for i in dic:
            print(dic[i], end=' ')
        print()
    def bottom_view(self):
        def recur(root, v, dic):
            if root == None:
                return
            dic[v] = root.val
            recur(root.right, v+1, dic)
            recur(root.left, v-1, dic)
        dic = {}
        recur(self.root, 0, dic)
        print("bottom view:", end=' ')
        for i in dic:
            print(dic[i], end=' ')
        print()
    def left_view(self):
        def recur(root, h, dic):
            if root == None:
                return
            recur(root.right, h+1, dic)
            dic[h] = root.val
            recur(root.left, h+1, dic)
        dic = {}
        recur(self.root, 0, dic)
        print("left view:", end=' ')
        for i in dic:
            print(dic[i], end=' ')
        print()
    def right_view(self):
        def recur(root, h, dic):
            if root == None:
                return
            recur(root.left, h+1, dic)
            dic[h] = root.val
            recur(root.right, h+1, dic)
        dic = {}
        recur(self.root, 0, dic)
        print("right view:", end=' ')
        for i in dic:
            print(dic[i], end=' ')
        print()

bst = BST()
print("enter values:", end=' ')
arr = list(map(int, input().split()))
for i in arr:
    bst.add(i)
bst.traverse()
bst.top_view()
bst.bottom_view()
bst.left_view()
bst.right_view()

