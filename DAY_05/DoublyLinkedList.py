
class node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class dll:
    def __init__(self):
        self.head = None
        self.tail = None
    def addback(self, x):
        if self.head == None:
            self.head = node(x)
            self.tail = self.head
        else:
            t = node(x)
            t.prev = self.tail
            self.tail.next = t
            self.tail = t
    def addfront(self, x):
        if self.head == None:
            self.head = node(x)
            self.tail = self.head
        else:
            t = node(x)
            t.next = self.head
            self.head.prev = t
            self.head = t
    def display(self):
        t = self.head
        while t != None:
            print(t.val, end=' ')
            t = t.next
        print()
    def reverse_display(self):
        t = self.tail
        while t != None:
            print(t.val, end=' ')
            t = t.prev
        print()
    def linear_search(self, target):
        left = self.head
        right = self.tail
        while left != right and left != right.next:
            if left.val == target or right.data == target:
                return True
            left = left.next
            right = right.prev
        if t.data == x:
            return True
        return False
    def even_or_odd_list(self):
        left = self.head
        right = self.tail
        while left != right and left != right.next:
            left = left.next
            right = right.prev
        if left != right:
            print("Odd Lengthed List")
        else:
            print("Even Lengthed List")
    def is_palindrome(self):
        left = self.head
        right = self.tail
        while left != right and left != right.next:
            if left.val != right.val:
                return False
            left = left.next
            right = right.prev
        if left != right:
            print("Odd Lengthed List")
        else:
            print("Even Lengthed List")
    def change_halves(self):
        slow = self.head
        fast = self.head
        while fast != self.tail and fast.next != self.tail:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next
        first = self.head
        second = slow
        while first != slow or second != None:
            first.val, second.val = second.val, first.val
            first = first.next
            second = second.next
    def swap_pairs(self):
        t = self.head
        head = t.next
        while t != None and t.next != None:
            t1 = t
            t2 = t.next
            t1temp = t1
            t2temp = t2
            if t1.prev != None:
                t1.prev.next = t2
            t2.prev = t1.prev
            t2.next = t1
            t1.prev = t2
            t1.next = t2temp.next
            t1.next.prev = t1
            t = t.next
    def valid_parentheses(self):
        temp = self.head
        index = 0
        stack = []
        while temp != None:
            if temp.val in "({[":
                stack.append(temp.val)
            else: 
                if stack:
                    x = stack.pop()
                    y = temp.val
                    if not ((x=='(' and y==')') or (x=='{' and y=='}') or (x=='[' and y==']')):
                        return index
                else:
                    return index
            index += 1
            temp = temp.next
        if not stack:
            return -1
        return index
    def even_odd_diff(self):
        def recur(head):
            if head == None:
                return 0
            if head.val % 2 == 0:
                return head.val + recur(head.next)
            else:
                return -head.val + recur(head.next)
        return abs(recur(self.head))
    def count_of_primes(self):
        def prime(num, i, end):
            if num <= 1:
                return False
            if i > end:
                return True
            if num % i == 0:
                return False
            return prime(num, i+1, end)
        def traverse(head, count):
            if head == None:
                return count
            if prime(head.val, 2, math.sqrt(head.val)):
                count += 1
            return traverse(head.next, count)
        return traverse(self.head, 0)

l = dll()

x = int(input())
while x != -1:
    l.addback(x)
    x = int(input())
print(l.count_of_primes())