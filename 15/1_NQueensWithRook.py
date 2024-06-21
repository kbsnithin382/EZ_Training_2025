# max queens that can be placed on n*n board when a rook is placed at given location

def possible(row, col):
    if board[row][col] == 'X':
        return False

    i = row - 1
    while i >= 0:
        if board[i][col] == 1:
            return False
        i -= 1

    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row - 1
    j = col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

max_q = 0
def queens(row, q):
    global max_q
    if row == len(board):
        return
    for col in range(len(board)):
        if possible(row, col):
            max_q = max(max_q, q+1)
            board[row][col] = 1
            queens(row+1, q+1)
            board[row][col] = 0


n = int(input("enter board size "))
board = [[0 for i in range(n)] for i in range(n)]
rook = list(map(int, input("enter rook location: ").split()))
for i in range(len(board)):
    board[i][rook[1]] = 'X'
for j in range(len(board)):
    board[rook[0]][j] = 'X'
queens(0, 0)
print(max_q)
