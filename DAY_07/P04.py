n = int(input())
l = []
for iter in range(n):
    order = input()
    s = input()
    z = ""
    for i in order:
        if i in s:
            x = i * s.count(i)
            z += x
    l.append(z)
print(l)