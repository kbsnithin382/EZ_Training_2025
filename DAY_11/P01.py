# graph traversal (DFS)

matrix = {5:[7,3], 7:[5,4,3], 4:[7,8,2], 8:[3,4,2], 3:[5,7,8], 2:[4,8]}

res = []
def recur(l, val):
    l.append(val)
    if val == 2:
        res.append(l[:])
    else:
        for i in matrix[val]:
            if i not in l:
                recur(l, i)
    l.pop()

recur([], 5)
print(res)

