"""

You are given a N*N maze with a rat placed at maze[0][0]. Find and print all paths that rat can follow to reach its destination i.e. maze[N-1][N-1]. Rat can move in any direc­tion ( left, right, up and down).
Value of every cell in the maze can either be 0 or 1. Cells with value 0 are blocked means rat can­not enter into those cells and those with value 1 are open.
"""
## Read input as specified in the question.
## Print output as specified in the question.

n = 0
maze = []

def printMaze(visited):
    global n
    for i in range(n):
        for j in range(n):
            if (i, j) in visited:
                print(1, end=" ")
            else:
                print(0, end=" ")
    print("")


def ratMaze(row, col, visited):
    if row == n-1 and col == n-1:
        visited.append((row, col))
        printMaze(visited)
        visited.pop()
        return
    if maze[row][col] == 1 and (row, col) not in visited:
        visited.append((row, col))
        previous_row = row - 1
        previous_col = col - 1
        next_row = row + 1
        next_col = col + 1
        if previous_row >= 0:
            ratMaze(previous_row, col, visited.copy())
        if previous_col >= 0:
            ratMaze(row, previous_col, visited.copy())
        if next_row < n:
            ratMaze(next_row, col, visited.copy())
        if next_col < n:
            ratMaze(row, next_col, visited.copy())
        visited.pop()


def main():
    global n
    global maze
    n = int(input())
    for i in range(n):
        maze.append(list(map(int, input().split())))
    if maze[0][0] != 0:
        ratMaze(0, 0, [])


if __name__ == "__main__":
    main()
