
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
m = len(l1)
n = len(l2)
res = []

def recur2(i, num):
    if i == n:
        return
    if (l2[i] + num) % 2 == 1:
        res.append(l2[i] + num)
    recur2(i+1, num)

def recur1(i):
    if i == n:
        return
    if l1[i] % 2 == 0:
        recur2(0, l1[i])
    recur1(i+1)

recur1(0)
print(res)
