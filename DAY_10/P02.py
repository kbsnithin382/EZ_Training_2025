"""
given a list of key value pairs
res = ""
append character in key at position of (max value <= len(key))
if no (max value <= len(key)) append x
return res
"""

s = list(map(str, input().split(',')))
n = len(s)
for i in range(n):
    s[i] = list(map(str, s[i].split(':')))
print(s)
res = ""
for i in s:
    max = 0
    for c in i[1]:
        if max < int(c) and int(c) <= len(i[0]):
            max = int(c)
    if max == 0:
        res += "x"
    else:
        res += i[0][max-1]
print(res)