

s = list(map(list, input().split()))
check = input()
n = len(s)

index = 0
for i in check:
    index %= n
    if i not in s[index]:
        print("NO")
        break
    s[index].remove(i)
    index += 1
else:
    print("YES")

