
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
m = len(l1)
n = len(l2)
res = []

def recur2(i, num, s):
    if i == n:
        res.append(s)
        return s
    if (l2[i] + num) % 2 == 1:
        s += l2[i] + num
    recur2(i+1, num, s)

def recur1(i):
    if i == m:
        return
    if l1[i] % 2 == 0:
        recur2(0, l1[i], 0)
    recur1(i+1)

recur1(0)
print(res)
