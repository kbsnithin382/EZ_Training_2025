# Next Number whose Sum of Digits is Prime
# Input: {-Z, Z}

import math

def sum_of_digits_is_prime(num):
    while num > 9:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        num = digit_sum
    return num in [2, 3, 5, 7]

num = int(input())
while True:
    if sum_of_digits_is_prime(num):
        print(num)
        break
    num += 1

