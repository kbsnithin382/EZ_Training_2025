
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
m = len(l1)
n = len(l2)
res = []

def recur(i, j, s):
    if i == m:
        return
    if j == n:
        res.append(s)
        recur(i+1, j, 0)
        return
    if l1[i] % 2 == 0 and l2[i] % 2 == 1:
        s += l1[i] + l2[j]
    recur(i, j+1, s)

recur(0,0,0)
print(res)
