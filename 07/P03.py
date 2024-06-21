"""
ip:
school
3
L 2 => rotates "school" to left by 2
R 2 => rotates "school" to right by 2
L 3
hoc => formed by first letter after each rotation
check if hoc is an anagram of any subsequence of school
"""

from collections import Counter

s = input()
n = int(input())
c = ""
sum = 0
for i in range(n):
    r = input()
    if r[0] == 'R':
        sum -= int(r[2])
        c += s[sum]
    else:
        sum += int(r[2])
        c += s[sum]
print(c)
count = Counter(c)

false = True
for i in range(0, len(s)-len(c)):
    if Counter(s[i:i+len(c)]) == count:
        print(True)
        false = False
        break
if false:
    print(False)