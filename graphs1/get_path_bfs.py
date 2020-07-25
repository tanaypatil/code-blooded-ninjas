"""
Code : Get Path - BFS
Send Feedback
Given an undirected graph G(V, E) and two vertices v1 and v2(as integers), find and print the path from v1 to v2 (if exists). Print nothing if there is no path between v1 and v2.
Find the path using BFS and print the shortest path available.
V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
E is the number of edges present in graph G.
Print the path in reverse order. That is, print v2 first, then intermediate vertices and v1 at last.
"""
## Read input as specified in the question.
## Print output as specified in the question.
from sys import stdin, stdout
from queue import Queue


def BFS(i, visited, adj_mat, v2):
    q = Queue()
    q.put(i)
    visited.append(i)
    vdict = {}
    while not q.empty():
        vertex = q.get()
        for i in range(len(adj_mat)):
            if i != vertex and i not in visited and adj_mat[vertex][i] == 1:
                q.put(i)
                vdict[i] = vertex
                visited.append(i)
                if i == v2:
                    return True, vdict
    return False, vdict


def main():
    v, e = map(int, stdin.readline().strip().split())
    adj_mat = [[0]*v for _ in range(v)]
    for i in range(e):
        v1, v2 = map(int, stdin.readline().strip().split())
        adj_mat[v1][v2] = 1
        adj_mat[v2][v1] = 1
    v1, v2 = map(int, stdin.readline().strip().split())
    ret, vdict = BFS(v1, [], adj_mat, v2)
    if ret:
        stdout.write(str(v2) + ' ')
        d = v2
        while True:
            if d == v1:
                break
            stdout.write(str(vdict[d]) + ' ')
            d = vdict[d]


if __name__ == "__main__":
    main()
