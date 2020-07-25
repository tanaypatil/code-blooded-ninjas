"""
Code : Has Path
Send Feedback
Given an undirected graph G(V, E) and two vertices v1 and v2(as integers), check if there exists any path between them or not. Print true or false.
V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
E is the number of edges present in graph G.
"""
## Read input as specified in the question.
## Print output as specified in the question.
from queue import Queue
from sys import stdin, stdout


def visit(i, visited, adj_mat, v, v2):
    visited.append(i)
    if i == v2:
        return True
    for j in range(v):
        if adj_mat[i][j] == 1 and j not in visited:
            if visit(j, visited, adj_mat, v, v2):
                return True
    return False


def main():
    v, e = map(int, stdin.readline().strip().split())
    adj_mat = [[0]*v for _ in range(v)]
    for i in range(e):
        v1, v2 = map(int, stdin.readline().strip().split())
        adj_mat[v1][v2] = 1
        adj_mat[v2][v1] = 1
    v1, v2 = map(int, stdin.readline().strip().split())
    if visit(v1, [], adj_mat, v, v2):
        print("true")
    else:
        print("false")



if __name__ == "__main__":
    main()
