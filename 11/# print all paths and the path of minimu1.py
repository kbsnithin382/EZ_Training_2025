# print all paths and the path of minimum cost

matrix = {  5:[(7,10),(3,5)],
            7:[(5,10),(4,3),(3,4)],
            4:[(7,3),(8,3),(2,1)],
            8:[(3,9),(4,3),(2,5)],
            3:[(5,5),(7,4),(8,9)],
            2:[(4,1),(8,5)]
         }

res = []
minpath = []
mincost = 99999
def recur(l, val, s):
    global mincost
    global minpath
    l.append(val[0])
    s += val[1]
    if val[0] == 2:
        x = l[:]
        x.extend([f"cost = {s}"])
        res.append(x)
        if mincost > s:
            mincost = s
            minpath = x[:]
    else:
        for i in matrix[val[0]]:
            if i[0] not in l:
                recur(l, i, s)
    l.pop()

print("All Paths:")
recur([], (5,0), 0)
for i in res:
    print(i[:-1], i[-1])
print("Min Path:", end=' ')
print(minpath[:-1], minpath[-1])

