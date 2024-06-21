# check if number can be presented as sum of 2 primes

import math

def prime(num):
    end = int(math.sqrt(num)) + 1
    for i in range(2, end):
        if num % i == 0:
            return False
    return True

num = int(input())

i = 1
j = num - 1
can = False
while(i < j):
    if prime(i) and prime(j):
        can = True
        break
    i += 1
    j -= 1

print(can)

