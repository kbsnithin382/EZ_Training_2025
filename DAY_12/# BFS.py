# BFS

dic = { 
    5: [(7,2), (3,1)],
    7: [(5,2), (4,6), (3,2)],
    4: [(7,6), (8,1), (2,2)],
    8: [(3,3), (4,1), (2,1)],
    3: [(5,1), (7,2), (8,3)],
    2: [(4,2), (8,1)]
}
queue = [(list(dic.keys())[0], 0)]
visited = {}
while queue:
    for i in dic[queue[0][0]]:
        if i[0] not in visited:
            queue.append((i[0],queue[0][1]+i[1]))
    x = queue.pop(0)
    if x[0] in visited:
        visited[x[0]] = min(visited[x[0]], x[1])
    else:
        visited[x[0]] = x[1]

print(f"BFS: {visited}")
