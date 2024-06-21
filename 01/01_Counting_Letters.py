
str1 = input()

i = 0
while i < len(str1):
    j = i
    count = 0
    while j < len(str1) and str1[j] == str1[i]:
        count += 1
        j += 1
    str1 = str1[:i+1] + str(count) + str1[j:]
    i += count

print(str1)