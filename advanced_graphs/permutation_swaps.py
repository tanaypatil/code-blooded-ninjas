"""
Permutation Swaps
Send Feedback
Kevin has a permutation P of N integers 1, 2, ..., N, but he doesn't like it. Kevin wants to get a permutation Q.

Also he believes that there are M good pairs of integers (ai , bi). Kevin can perform following operation with his permutation:

Swap Px and Py only if (x, y) is a good pair.
Help him and tell if Kevin can obtain permutation Q using such operations.
"""
## Read input as specified in the question.
## Print output as specified in the question.
from collections import defaultdict


def visit(i, visited, adj, cc):
    visited[i] = True
    cc.append(i)
    for j in adj[i]:
        if not visited[j]:
            visit(j, visited, adj, cc)
    


if __name__ == "__main__":
    tc = int(input())
    for t in range(tc):
        n, m = map(int, input().split())
        P = list(map(int, input().strip().split()))
        Q = list(map(int, input().strip().split()))
        adj = defaultdict(list)
        for i in range(m):
            a, b = map(int, input().strip().split())
            adj[a-1].append(b-1)
            adj[b-1].append(a-1)
        visited = defaultdict(bool)
        components = []
        for i in range(n):
            if not visited[i]:
                cc = []
                visit(i, visited, adj, cc)
                components.append(cc)
        f = 0
        for component in components:
            pc, qc = [], []
            for v in component:
                pc.append(P[v])
                qc.append(Q[v])
            pc.sort()
            qc.sort()
            if pc != qc:
                f = 1
                break
        if f == 1:
            print("NO")
        else:
            print("YES")
        
