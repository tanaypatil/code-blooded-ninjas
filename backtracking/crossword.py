"""

CodingNinjas has provided a crossword of 10*10 grid. The grid contains '+' or '-' as its cell values. Now, you are also provided with a word list that needs to placed accurately in the grid. Cells marked with '-' are to be filled with word list.
"""

def isFull(board):
    for b in board:
        for e in b:
            if e == "-":
                return False
    return True


def is_valid_vertical(board, word, row, col):
    inserted = []
    if len(word) + row > 10:
        return inserted, False
    for i in range(row, row + len(word)):
        if board[i][col] == "-" or board[i][col] == word[i-row]:
            if board[i][col] == "-":
                inserted.append(i)
        else:
            return inserted, False
    return inserted, True


def set_vertical(board, word, row, col):
    for i in range(row, row + len(word)):
        board[i][col] = word[i-row]


def reset_vertical(board, inserted, col):
    for i in inserted:
        board[i][col] = "-"


def is_valid_horizontal(board, word, row, col):
    inserted = []
    if len(word) + col > 10:
        return inserted, False
    for i in range(col, col + len(word)):
        if board[row][i] == "-" or board[row][i] == word[i-col]:
            if board[row][i] == "-":
                inserted.append(i)
        else:
            return inserted, False
    return inserted, True


def set_horizontal(board, word, row, col):
    for i in range(col, col + len(word)):
        board[row][i] = word[i-col]


def reset_horizontal(board, inserted, row):
    for i in inserted:
        board[row][i] = "-"


def solveGrid(board, words):
    if len(words) == 0 and isFull(board):
        return True
    for row, b in enumerate(board):
        for col, e in enumerate(b):
            if e == "-" or e == words[0][0]:
                inserted, valid = is_valid_vertical(board, words[0], row, col)
                if valid:
                    set_vertical(board, words[0], row, col)
                    if solveGrid(board, words[1:]):
                        return True
                    reset_vertical(board, inserted, col)
                inserted, valid = is_valid_horizontal(board, words[0], row, col)
                if valid:
                    set_horizontal(board, words[0], row, col)
                    if solveGrid(board, words[1:]):
                        return True
                    reset_horizontal(board, inserted, row)
    return False


def main():
    board = [list(input()) for i in range(10)]
    words = input().split(';')
    if solveGrid(board, words):
        for b in board:
            print(''.join(b))


if __name__ == "__main__":
    main()
