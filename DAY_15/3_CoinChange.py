# check if given amount of money can be formed using given coins (only one unit of each coin)

l = list(map(int, input().split()))
target = int(input())

def recur(x, index):
    if sum(x) == target:
        return True
    if index == len(l):
        return False
    return recur(x, index+1) or recur(x+[l[index]], index+1)

print(recur([], 0))
