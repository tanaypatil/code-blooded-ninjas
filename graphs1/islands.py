"""
Islands
Send Feedback
An island is a small piece of land surrounded by water . A group of islands is said to be connected if we can reach from any given island to any other island in the same group . Given N islands (numbered from 1 to N) and two lists of size M (u and v) denoting island u[i] is connected to island v[i] and vice versa . Can you count the number of connected groups of islands.
"""
## Read input as specified in the question.
## Print output as specified in the question.

from sys import stdin, stdout
from queue import Queue


def BFS(i, visited, adj_mat):
    q = Queue()
    q.put(i)
    visited.append(i)
    while not q.empty():
        vertex = q.get()
        for i in range(len(adj_mat)):
            if i != vertex and i not in visited and adj_mat[vertex][i] == 1:
                q.put(i)
                visited.append(i)
                
         
def main():
    n, m = map(int, input().strip().split())
    u = list(map(int, input().strip().split()))
    v = list(map(int, input().strip().split()))
    adj_mat = [[0]*n for _ in range(n)]
    for i in range(m):
        v1, v2 = u[i], v[i]
        adj_mat[v1-1][v2-1] = 1
        adj_mat[v2-1][v1-1] = 1
    comm = []
    count = 0
    for i in range(n):
        if i not in comm:
            visited = []
            BFS(i, visited, adj_mat)
            comm += visited
            count += 1
    print(count)
                
                
if __name__ == "__main__":
    main()
