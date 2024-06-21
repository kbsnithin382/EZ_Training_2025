
s1 = input()
s2 = input()
n1 = len(s1)
n2 = len(s2)

mat = [[0 for j in range(n2+1)] for i in range(n1+1)]

for i in range(1, n1+1):
    for j in range(1, n2+1):
        mat[i][j] = max(mat[i-1][j], mat[i][j-1])
        if s1[i-1] == s2[j-1]:
            mat[i][j] += 1

s = ""
i = n1
j = n2
while i and j:
    if s1[i-1] == s2[j-1]:
        s += s1[i-1]
        i -= 1
        j -= 1
    else:
        if mat[i][j-1] == mat[i][j]:
            j -= 1
        else:
            i -= 1

print(mat[n1][n2])
print(s[::-1])

