# given a string => aaabbcd
# output => a3b2c1d1

str1 = input()

# Sliding Window Algo
res = str1[0]
count = 1
i = 1
while i < len(str1):
    if str1[i] == str1[i-1]:
        count += 1
    else:
        res += str(count) + str1[i]
        count = 1
    i += 1
res += str(count)

print(res)