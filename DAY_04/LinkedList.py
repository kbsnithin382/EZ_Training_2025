# LinkedList

class node:

    def __init__(self, val):
        self.data = val
        self.nxt = None

class sll:

    def __init__(self):
        self.head = None
    
    def length(self):
        count = 0
        t = self.head
        while t != None:
            count += 1
            t = t.nxt
        return count

    def display(self):
        t = self.head
        while t != None:
            print(t.data, end=' -> ')
            t = t.nxt
        print()

    def addfront(self, x):
        tn = node(x)
        tn.nxt = self.head
        self.head = tn

    def addback(self, x):
        if self.head == None:
            self.head = node(x)
            return
        t = self.head
        while t.nxt != None:
            t = t.nxt
        t.nxt = node(x)

    def search(self, x):
        t = self.head
        found = False
        while t != None:
            if t.data == x:
                print("Found")
                found = True
                break
            t = t.nxt
        if not found:
            print("Not Found")

    def middle(self):
        slow = self.head
        fast = slow.nxt
        while fast != None:
            slow = slow.nxt
            if fast.nxt == None:
                fast = fast.nxt
            else:
                fast = fast.nxt.nxt
        print(slow.data)

    def print_pairs(self):
        t = self.head
        while t != None:
            t1 = t
            while t1 != None:
                print((t.data, t1.data), end=' ')
                t1 = t1.nxt
            t = t.nxt

    def len_eo(self):
        slow = self.head
        fast = slow.nxt
        while fast != None and fast.nxt != None:
            fast = fast.nxt.nxt
            slow = slow.nxt
        print()
        if fast == None:
            print("odd lengthed list")
        else:
            print("even lengthed list")

    def long_seq_len(self):
        count = 1
        max_count = 1
        t = self.head
        prev = t.data
        t = t.nxt
        while t != None:
            if t.data == (prev + 1):
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
            max_count = max(max_count, count)
            prev = t.data
            t = t.nxt
        print(max_count)

    def bubble_sort(self):
        start = self.head
        end = None
        while t != None:
            prev = self.head
            t = prev.nxt
            sorted = True
            for i in range(n-1):
                if prev.data > t.data:
                    prev.data, t.data = t.data, prev.data
                    sorted = False
                prev = t
                t = t.nxt
            if sorted:
                break
            n -= 1
        self.display()


l1 = sll()
l1.head = node(10)
l1.addfront(0)
l1.addback(5)
l1.display()
l1.search(int(input("search element? ")))
l1.middle()
l1.print_pairs()
l1.len_eo()
l1.long_seq_len()
l1.bubble_sort()