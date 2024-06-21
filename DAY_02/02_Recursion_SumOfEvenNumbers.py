# Sum of Even Numbers in given range

def sum_of_even(num):
    if num == 1:
        return 0
    if num % 2 == 0:
        return num + sum_of_even(num - 1)
    return sum_of_even(num - 1)

print(sum_of_even(int(input())))
