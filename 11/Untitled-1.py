
path = []
def recur(matrix, l, start, end):
    if l and l[-1] == end:
        path.append(l)
        return
    l.append(start)
    for i in matrix[l[-1]]:
        if i not in l:
            recur(matrix, l, i, end)

matrix = {5:[7,3], 7:[5,4,3], 4:[7,8,2], 8:[3,4,2], 3:[5,7,8], 2:[4,8]}
recur(matrix, [], 5, 2)
print(*path)