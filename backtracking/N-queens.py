"""
You are given N, and for a given N x N chessboard, find a way to place N queens such that no queen can attack any other queen on the chess board. A queen can be killed when it lies in the same row, or same column, or the same diagonal of any of the other queens. You have to print all such configurations.
"""


def canPlace(r,c):
    for j in range(n):
        if board[r][j] == 1 or board[j][c] == 1:
            return False
        if 0 <= r+c-j < n:
            if board[j][r+c-j] == 1:
                return False
        if 0 <= j-(r-c) < n:
            if board[j][j-(r-c)] == 1:
                return False
    return True


def printBoard():
    for b in board:
        print(*b, end=" ")
    print("")
    

def resetBoard():
    for b in board:
        for j in range(n):
            b[j] = 0


    
def nQueen(row):
    #Implement Your Code Here
    global board
    if row >= n:
        return True
    for i in range(n):
        if canPlace(row, i):
            board[row][i] = 1
            if nQueen(row+1):
                if row == n-1:
                    printBoard()
                else:
                    return True
            board[row][i] = 0
            if row == 0:
                resetBoard()
    return False


n = int(input())
board = []
for j in range(n):
    board.append([0]*n)
nQueen(0)
