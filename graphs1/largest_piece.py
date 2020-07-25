"""
Largest Piece
Send Feedback
Its Gary's birthday today and he has ordered his favourite square cake consisting of '0's and '1's . But Gary wants the biggest piece of '1's and no '0's . A piece of cake is defined as a part which consist of only '1's, and all '1's share an edge with eachother on the cake. Given the size of cake N and the cake , can you find the size of the biggest piece of '1's for Gary ?
"""
## Read input as specified in the question.
## Print output as specified in the question.

def backtrack(board, row, col, visited):
    global max_count
    n, m = len(board), len(board[0])
    
    visited.append((row, col))
    
    i1, j1 = row, col-1
    i2, j2 = row, col+1
    i4, j4 = row-1, col
    i7, j7 = row+1, col
    
    c1 = c2 = c3 = c4 = 0
    
    if 0 <= i1 < n and 0 <= j1 < m:
        if board[i1][j1] == "1" and (i1, j1) not in visited:
            c1 = backtrack(board, i1, j1, visited)
    if 0 <= i2 < n and 0 <= j2 < m:
        if board[i2][j2] == "1" and (i2, j2) not in visited:
            c2 = backtrack(board, i2, j2, visited)
    if 0 <= i4 < n and 0 <= j4 < m:
        if board[i4][j4] == "1" and (i4, j4) not in visited:
            c3 = backtrack(board, i4, j4, visited)
    if 0 <= i7 < n and 0 <= j7 < m:
        if board[i7][j7] == "1" and (i7, j7) not in visited:
            c4 = backtrack(board, i7, j7, visited)
    
    return 1 + c1 + c2 + c3 + c4




def main():
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]
    comm = []
    visited = []
    max_count = 0
    for row, line in enumerate(board):
        for col, num in enumerate(line):
             if board[row][col] == "1" and (row, col) not in comm:
                 max_count = max(backtrack(board, row, col, visited), max_count)
                 comm += visited
                 visited = []
    print(max_count)



if __name__ == "__main__":
    main()
