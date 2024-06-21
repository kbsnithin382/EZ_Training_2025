
n = int(input())

num = 1
for i in range(n):
    if i == 0:
        print('* ' * n)
    elif i == (n - 1):
        print('* ' * n)
    else:
        print('*', end = ' ')
        for i in range(1, n-1):
            print(num, end=' ')
            num += 1
        print('*')