import math

# Recursive Function
def next_prime(num):
    end = math.floor(math.sqrt(num)) + 1
    for i in range(2, end):
        if num % i == 0:
            return next_prime(num+1) # recursion call
    return num

num = int(input())
print(next_prime(num))