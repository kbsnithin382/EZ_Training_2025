# count number of occurances of each number

l = list(map(int, input().split()))

dic = {}
for i in l:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for i in dic:
    print(str(i) + " - " + str(dic[i]))