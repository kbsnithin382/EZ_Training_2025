def recur(num, rev):
    if num == 0:
        return rev
    rev = rev * 10 + num % 10
    return recur(num // 10, rev)

num = int(input())
print(num == recur(num, 0))