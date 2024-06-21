# total possible ways to place n queens on n*n board

def possible(row, col):
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
    
c = 0
boards = []
def queens(row):
    global c
    if row == len(board):
        boards.append([x[:] for x in board])
        c += 1
        return
    for col in range(len(board)):
        if possible(row, col):
            board[row][col] = 1
            queens(row+1)
            board[row][col] = 0


n = int(input("enter number of queens "))
board = [[0 for i in range(n)] for i in range(n)]
queens(0)
print(boards)

