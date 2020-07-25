"""
Connecting Dots
Send Feedback
Gary has a board of size NxM. Each cell in the board is a coloured dot. There exist only 26 colours denoted by uppercase Latin characters (i.e. A,B,...,Z). Now Gary is getting bore and wants to play a game. The key of this game is to find a cycle that contain dots of same colour. Formally, we call a sequence of dots d1, d2, ..., dk a cycle if and only if it meets the following condition:
1. These k dots are different: if i ≠ j then di is different from dj.
2. k is at least 4.
3. All dots belong to the same colour.
4. For all 1 ≤ i ≤ k - 1: di and di + 1 are adjacent. Also, dk and d1 should also be adjacent. Cells x and y are called adjacent if they share an edge.
Since Gary is colour blind, he wants your help. Your task is to determine if there exists a cycle on the board.
"""
## Read input as specified in the question.
## Print output as specified in the question.

def backtrack(letter, row, col, board, visited):
    n, m = len(board), len(board[0])
    i1, j1 = row, col-1
    i2, j2 = row, col+1
    i4, j4 = row-1, col
    i7, j7 = row+1, col
    
    visited.append((row, col))
    
    if 0 <= i1 < n and 0 <= j1 < m:
        if board[i1][j1] == letter:
            if (i1, j1) == visited[0] and len(visited) >= 4:
                return True
            elif (i1, j1) not in visited and backtrack(letter, i1, j1, board, visited):
                return True
    if 0 <= i2 < n and 0 <= j2 < m:
        if board[i2][j2] == letter:
            if (i2, j2) == visited[0] and len(visited) >= 4:
                return True
            elif (i2, j2) not in visited and backtrack(letter, i2, j2, board, visited):
                return True
    if 0 <= i4 < n and 0 <= j4 < m:
        if board[i4][j4] == letter:
            if (i4, j4) == visited[0] and len(visited) >= 4:
                return True
            elif (i4, j4) not in visited and backtrack(letter, i4, j4, board, visited):
                return True
    if 0 <= i7 < n and 0 <= j7 < m:
        if board[i7][j7] == letter:
            if (i7, j7) == visited[0] and len(visited) >= 4:
                return True
            elif (i7, j7) not in visited:
                if backtrack(letter, i7, j7, board, visited):
                    return True
                
    visited.pop()
    return False



def base(board):
    for row, line in enumerate(board):
        for col, letter in enumerate(line):
            if backtrack(letter, row, col, board, []):
                return True
    return False



def main():
    n, m = map(int, input().strip().split())
    board = [list(input().strip()) for _ in range(n)]
    if base(board):
        print(1)
    else:
        print(0)




if __name__ == "__main__":
    main()
