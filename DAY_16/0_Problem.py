"""
n => number of queries => 7
1 school
1 world
1 word
1 scholar
2 word
2 wood
3 sch

1 insert
2 search
3 prefix search
4 delete
"""

n = int(input())
l = []
for i in range(n):
    l.append(input().split())
    l[i][0] = int(l[i][0])

storage = set()
for i in l:
    if i[0] == 1:
        storage.add(i[1])
    elif i[0] == 2:
        print(i[1] in storage)
    elif i[0] == 3:
        c = 0
        for word in storage:
            if i[1] == word[:len(i[1])]:
                c += 1
        print(c)
    elif i[0] == 4:
        if i[1] in storage:
            storage.discard(i[1])