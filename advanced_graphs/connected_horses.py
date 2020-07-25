"""
Connected horses
Send Feedback
You all must be familiar with the chess-board having 
8*8 squares of alternate black and white cells. Well, here 
we have for you a similar 
N*M size board with similar arrangement of black and white 
cells.
A few of these cells have Horses placed over them. 
Each horse is unique. Now these horses are not the 
usual horses which could jump to any of the 
8 positions they usually jump in. They can move only if there is another horse on one of the 8-positions that it can     go to usually and then both the horses will swap their positions. This swapping can happen infinitely times.
A photographer was assigned to take a picture of all the different ways that the horses occupy the board! Given the state of the board, calculate answer. Sincethis answer may be quite large, calculate in modulo 
10^9+7
"""
## Read input as specified in the question.
## Print output as specified in the question.
import sys
from collections import defaultdict


def factorial(n):
    f = 1
    c = 1
    for c in range(1, n+1):
        f = f*c
    return f


def visit(x, y, visited, cc, adj):
    visited[(x, y)] = True
    cc.append((x, y))
    for j in adj[(x, y)]:
        if not visited[(j[0], j[1])]:
            visit(j[0], j[1], visited, cc, adj)



if __name__ == "__main__":
    sys.setrecursionlimit(50000)
    tc = int(sys.stdin.readline())
    for t in range(tc):
        n, m, q = map(int, sys.stdin.readline().strip().split())
        horses = defaultdict(bool)
        adj = defaultdict(list)
        for i in range(q):
            x, y = map(int, sys.stdin.readline().strip().split())
            x -= 1
            y -= 1
            horses[(x, y)] = True
            I = [2, 2, -2, -2, -1, 1, -1, 1]
            J = [-1, 1, -1, 1, -2, -2, 2, 2]
            for j in range(8):
                p, q = x + I[j], y + J[j]
                if 0 <= p < n and 0 <= q < m and horses[(p, q)]:
                    adj[(x, y)].append((p, q))
                    adj[(p, q)].append((x, y))
        visited = defaultdict(bool)
        ret = 1
        for i in range(n):
            for j in range(m):
                if horses[(i, j)] and not visited[(i, j)]:
                    cc = []
                    visit(i, j, visited, cc, adj)
                    ret *= factorial(len(cc))
        sys.stdout.write(str(ret%(10**9+7))+"\n")
