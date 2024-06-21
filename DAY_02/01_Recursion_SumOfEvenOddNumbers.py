# print sums of even, odd numbers using Recursion
# (length of lists are equal)

def even_odd_sum(i, s1, s2):
    if i == len(a):
        return s1, s2
    else:
        if a[i] % 2 == 0:
            s1 += a[i]
        if b[i] % 2 == 1:
            s2 += b[i]
    return even_odd_sum(i+1, s1, s2)

a = [1, 2, 3]
b = [4, 5, 6]
print(even_odd_sum(0, 0, 0))
