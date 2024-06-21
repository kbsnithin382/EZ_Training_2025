class BST_X:
    def sum_values(self):
        def sum(head):
            if head == None:
                return 0
            return head.val + sum(head.left) + sum(head.right)
        res = sum(self.head)
        print("sum =", res)
    def sum_even_odd_values(self):
        def sum(head):
            if head == None:
                return 0, 0
            if head.val % 2 == 0:
                return head.val + (sum(head.left) + sum(head.right))[0], (sum(head.left) + sum(head.right))[1]
            else:
                return (sum(head.left) + sum(head.right))[0], head.val + (sum(head.left) + sum(head.right))[1]
        print(sum(self.head))
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