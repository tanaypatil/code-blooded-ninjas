"""
FILLMTR
Send Feedback
Fill The Matrix
A matrix B (consisting of integers) of dimension N × N is said to be good if there exists an array A (consisting of integers) such that B[i][j] = |A[i] - A[j]|, where |x| denotes absolute value of integer x.

You are given a partially filled matrix B of dimension N × N. Q of the entries of this matrix are filled by either 0 or 1. You have to identify whether it is possible to fill the remaining entries of matrix B (the entries can be filled by any integer, not necessarily by 0 or 1) such that the resulting fully filled matrix B is good.
"""
from collections import defaultdict
import operator


def get_parent(a, parent):
    while a != parent[a]:
        a = parent[a]
    return a


def set_parent(a, b, parent):
    p1 = get_parent(a, parent)
    p2 = get_parent(b, parent)
    parent[p1] = p2


def fill_matrix(elements, n):
    adj = defaultdict(list)
    parent = [i for i in range(n)]
    visited = defaultdict(bool)
    for a, b, w in elements:
        if w == 0:
            set_parent(a, b, parent)
        else:
            if a == b:
                return False
            else:
                p1 = get_parent(a, parent)
                p2 = get_parent(b, parent)
                adj[p1].append(p2)
                adj[p2].append(p1)
                
    return is_bipartite(parent, adj, n) 


def is_bipartite(parent, adj, n):
    visited = defaultdict(bool)
    for i in range(n):
        if not visited[i]:
            sets = [[parent[i]], []]
            pending = [parent[i]]
            visited = defaultdict(bool)
            while len(pending) > 0:
                current = pending.pop()
                currentSet = 0 if current in sets[0] else 1
                for j in adj[current]:
                    if j not in sets[0] and j not in sets[1]:
                        sets[1-currentSet].append(j)
                        pending.append(j)
                    elif j in sets[currentSet]:
                        return False
    return True
    


if __name__ == "__main__":
    tc = int(input())
    for t in range(tc):
        n, q = map(int, input().strip().split())
        elements = []
        for i in range(q):
            a, b, w = map(int, input().strip().split())
            elements.append((a-1, b-1, w))
        elements = sorted(elements, key=operator.itemgetter(2))
        if fill_matrix(elements, n):
            print("yes")
        else:
            print("no")
