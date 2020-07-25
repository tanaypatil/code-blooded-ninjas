"""
Given a 9*9 sudoku board, in which some entries are filled and others are 0 (0 indicates that the cell is empty), you need to find out whether the Sudoku puzzle can be solved or not i.e. return true or false.
"""

def findEmpty(board):
    for row,b in enumerate(board):
        for col,j in enumerate(b):
            if j == 0:
                return row, col
    return -1, -1
            

def canPlace(row, col, a, board):
    for i in range(9):
        if board[row][i] == a:
            return False
    for i in range(9):
        if board[i][col] == a:
            return False
    col_start = (col//3)*3
    col_end = col_start + 2
    row_start = (row//3)*3
    row_end = row_start + 2
    for r in range(row_start, row_end+1):
        for c in range(col_start, col_start+1):
            if board[r][c] == a:
                return False
    return True



def solveSudoku(board):
    row, col = findEmpty(board)
    if row == -1 and col == -1:
        return True
    for i in range(1, 10):
        if canPlace(row, col, i, board):
            board[row][col] = i
            if solveSudoku(board):
                return True
            board[row][col] = 0
    return False
    

board = [[ int(ele) for ele in input().split() ]for i in range(9)]
ans = solveSudoku(board)
if ans is True:
    print('true')
else:
    print('false')
