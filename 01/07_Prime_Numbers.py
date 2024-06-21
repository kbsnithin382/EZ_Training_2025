import math

def is_prime(num):
    sqrt = math.floor(math.sqrt(num))
    for i in range(2, sqrt + 1):
        if num % i == 0:
            return False
    return True

num = int(input())
while True:
    if is_prime(num):
        print(num)
        break
    num += 1
