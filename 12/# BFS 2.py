

def bfs(dic, visited, queue, val):
    for i in dic[val]:
        if i[0] not in visited and i[0] not in queue:
            queue.append(i[0])
    visited.append(queue.pop(0))
    if not queue:
        return visited
    return bfs(dic, visited, queue, queue[0])

dic = { 
    5: [(7,2), (3,1)],
    7: [(5,2), (4,6), (3,2)],
    4: [(7,6), (8,1), (2,2)],
    8: [(3,3), (4,1), (2,1)],
    3: [(5,1), (7,2), (8,3)],
    2: [(4,2), (8,1)]
}
queue = [list(dic.keys())[0]]
visited = bfs(dic, [], queue, queue[0])
print(f"BFS: {visited}")