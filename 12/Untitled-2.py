
def make_zeroes(l, i, j, count):
    if i == -1 or j == -1 or i == len(l) or j == len(l) or l[i][j] == 0:
        return count
    if l[i][j] == 1:
        l[i][j] = 0
        count = max(count, make_zeroes(l, i-1, j, count))
        count = max(count, make_zeroes(l, i, j+1, count))
        count = max(count, make_zeroes(l, i+1, j, count))
        count = max(count, make_zeroes(l, i, j-1, count))
        return count + 1
    
n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

islands = 0
area = 0
for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            islands += 1
            area = max(area, make_zeroes(mat, i, j, 0))

print(f"islands = {islands}")
print(f"largest area = {area}")