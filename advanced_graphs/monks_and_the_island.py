"""
Monk and the Islands
Send Feedback
MONK AND THE ISLAND
Monk visits the land of Islands. There are a total of N islands numbered from 1 to N. Some pairs of islands are connected to each other by Bidirectional bridges running over water.
Monk hates to cross these bridges as they require a lot of efforts. He is standing at Island #1 and wants to reach the Island #N. Find the minimum the number of bridges that he shall have to cross, if he takes the optimal route.
"""
## Read input as specified in the question.
## Print output as specified in the question.
import sys
from collections import defaultdict


def bfs(adj, n):
    q = [0]
    visited = defaultdict(bool)
    d = 0
    while len(q) > 0:
        size = len(q)
        for i in range(size):
            v = q[0]
            q = q[1:]
            visited[v] = True
            for j in adj[v]:
                if j == n-1:
                    return d+1
                if not visited[j]:
                    q.append(j)
                    visited[j] = True
        d += 1
    return d



if __name__ == "__main__":
    sys.setrecursionlimit(50000)
    tc = int(input())
    for t in range(tc):
        n, m = map(int, input().strip().split())
        adj = defaultdict(list)
        for i in range(m):
            x, y = map(int, input().strip().split())
            adj[x-1].append(y-1)
            adj[y-1].append(x-1)
        print(bfs(adj, n))
        
