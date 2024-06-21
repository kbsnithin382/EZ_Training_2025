# top, right, bottom, left views of a binary tree using queues

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
        if self.root == None:
            return
        dic = {}
        queue = [(self.root, 0)]
        while queue:
            node, vlevel = queue.pop(0)
            if node.left:
                queue.append((node.left, vlevel-1))
            if node.right:
                queue.append((node.right, vlevel+1))
            if vlevel not in dic:
                dic[vlevel] = node
        print("top view:", end=' ')
        for i in sorted(list(dic.keys())):
            print(dic[i].val, end=' ')
        print()
            
    def bottom_view(self):
        if self.root == None:
            return
        dic = {}
        queue = [(self.root, 0)]
        while queue:
            node, vlevel = queue.pop(0)
            if node.left:
                queue.append((node.left, vlevel-1))
            if node.right:
                queue.append((node.right, vlevel+1))
            dic[vlevel] = node
        print("bottom view:", end=' ')
        for i in sorted(list(dic.keys())):
            print(dic[i].val, end=' ')
        print()
    
    def left_view(self):
        if self.root == None:
            return
        dic = {}
        queue = [(self.root, 0)]
        while queue:
            node, hlevel = queue.pop(0)
            if node.left:
                queue.append((node.left, hlevel+1))
            if node.right:
                queue.append((node.right, hlevel+1))
            if hlevel not in dic:
                dic[hlevel] = node
        print("left view:", end=' ')
        for i in sorted(list(dic.keys())):
            print(dic[i].val, end=' ')
        print()
    
    def right_view(self):
        if self.root == None:
            return
        dic = {}
        queue = [(self.root, 0)]
        while queue:
            node, hlevel = queue.pop(0)
            if node.left:
                queue.append((node.left, hlevel+1))
            if node.right:
                queue.append((node.right, hlevel+1))
            dic[hlevel] = node
        print("right view:", end=' ')
        for i in sorted(dic.keys()):
            print(dic[i].val, end=' ')
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

