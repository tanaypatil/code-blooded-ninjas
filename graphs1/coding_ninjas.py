"""
Coding Ninjas
Send Feedback
Given a NxM matrix containing Uppercase English Alphabets only. Your task is to tell if there is a path in the given matrix which makes the sentence “CODINGNINJA” .
There is a path from any cell to all its neighbouring cells. A neighbour may share an edge or a corner.
"""
def coding(i, x, y, target, visited, board):
    n = len(board)
    m = len(board[0])
    if i == len(target)-1:
        return True
    i1, j1 = x, y-1
    i2, j2 = x, y+1
    i3, j3 = x-1, y
    i4, j4 = x-1, y-1
    i5, j5 = x-1, y+1
    i6, j6 = x+1, y
    i7, j7 = x+1, y-1
    i8, j8 = x+1, y+1
    visited.append((x, y))
    if 0 <= i1 < n and 0 <= j1 < m and (i1, j1) not in visited:
        if board[i1][j1] == target[i+1]:
            if coding(i+1, i1, j1, target, visited, board):
                return True
    if 0 <= i2 < n and 0 <= j2 < m and (i2, j2) not in visited:
        if board[i2][j2] == target[i+1]:
            if coding(i+1, i2, j2, target, visited, board):
                return True
    if 0 <= i3 < n and 0 <= j3 < m and (i3, j3) not in visited:
        if board[i3][j3] == target[i+1]:
            if coding(i+1, i3, j3, target, visited, board):
                return True
    if 0 <= i4 < n and 0 <= j4 < m and (i4, j4) not in visited:
        if board[i4][j4] == target[i+1]:
            if coding(i+1, i4, j4, target, visited, board):
                return True
    if 0 <= i5 < n and 0 <= j5 < m and (i5, j5) not in visited:
        if board[i5][j5] == target[i+1]:
            if coding(i+1, i5, j5, target, visited, board):
                return True
    if 0 <= i6 < n and 0 <= j6 < m and (i6, j6) not in visited:
        if board[i6][j6] == target[i+1]:
            if coding(i+1, i6, j6, target, visited, board):
                return True
    if 0 <= i7 < n and 0 <= j7 < m and (i7, j7) not in visited:
        if board[i7][j7] == target[i+1]:
            if coding(i+1, i7, j7, target, visited, board):
                return True
    if 0 <= i8 < n and 0 <= j8 < m and (i8, j8) not in visited:
        if board[i8][j8] == target[i+1]:
            if coding(i+1, i8, j8, target, visited, board):
                return True
    visited.pop()
    return False
    


def ninjas(i, board, visited, target):
    n = len(board)
    m = len(board[0])
    for index1, line in enumerate(board):
        for index2, word in enumerate(line):
            visited.append((index1, index2))
            if word == target[i]:
                i1, j1 = index1, index2-1
                i2, j2 = index1, index2+1
                i3, j3 = index1-1, index2
                i4, j4 = index1-1, index2-1
                i5, j5 = index1-1, index2+1
                i6, j6 = index1+1, index2
                i7, j7 = index1+1, index2-1
                i8, j8 = index1+1, index2+1
                if 0 <= i1 < n and 0 <= j1 < m:
                    if board[i1][j1] == target[i+1]:
                        if coding(i+1, i1, j1, target, visited, board):
                            return True
                if 0 <= i2 < n and 0 <= j2 < m:
                    if board[i2][j2] == target[i+1]:
                        if coding(i+1, i2, j2, target, visited, board):
                            return True
                if 0 <= i3 < n and 0 <= j3 < m:
                    if board[i3][j3] == target[i+1]:
                        if coding(i+1, i3, j3, target, visited, board):
                            return True
                if 0 <= i4 < n and 0 <= j4 < m:
                    if board[i4][j4] == target[i+1]:
                        if coding(i+1, i4, j4, target, visited, board):
                            return True
                if 0 <= i5 < n and 0 <= j5 < m:
                    if board[i5][j5] == target[i+1]:
                        if coding(i+1, i5, j5, target, visited, board):
                            return True
                if 0 <= i6 < n and 0 <= j6 < m:
                    if board[i6][j6] == target[i+1]:
                        if coding(i+1, i6, j6, target, visited, board):
                            return True
                if 0 <= i7 < n and 0 <= j7 < m:
                    if board[i7][j7] == target[i+1]:
                        if coding(i+1, i7, j7, target, visited, board):
                            return True
                if 0 <= i8 < n and 0 <= j8 < m:
                    if board[i8][j8] == target[i+1]:
                        if coding(i+1, i8, j8, target, visited, board):
                            return True
            visited.pop()
    return False



def main():
    n, m = map(int, input().strip().split())
    board = [list(input().strip()) for _ in range(n)]
    if ninjas(0, board, [], "CODINGNINJA"):
        print(1)
    else:
        print(0)




if __name__ == "__main__":
    main()
