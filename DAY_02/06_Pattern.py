"""
input: 4
____a____
___bab___
__cbabc__
_dcbabcd_
"""

n = int(input())

for i in range(n):
    print('_' * (n - i), end='')
    j = ord('a') + i
    for k in range(j, ord('a'), -1):
        print(chr(k), end='')
    for k in range(ord('a'), j+1, 1):
        print(chr(k), end='')
    print('_' * (n - i))

