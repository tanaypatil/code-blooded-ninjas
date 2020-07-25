"""
Code : Is Connected ?
Send Feedback
Given an undirected graph G(V,E), check if the graph G is connected graph or not.
V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
E is the number of edges present in graph G.
"""
## Read input as specified in the question.
## Print output as specified in the question.
from queue import Queue


def visit(i, visited, adj_mat, v):
    visited.add(i)
    for j in range(v):
        if adj_mat[i][j] == 1 and j not in visited:
            visit(j, visited, adj_mat, v)


def main():
    v, e = map(int, input().strip().split())
    adj_mat = [[0]*(v) for _ in range(v)]
    for i in range(e):
        v1, v2 = map(int, input().strip().split())
        adj_mat[v1][v2] = 1
        adj_mat[v2][v1] = 1
    visited = set()
    visit(0, visited, adj_mat, v)
    if len(visited) == v:
        print("true")
    else:
        print("false")
    
    
        

if __name__ == "__main__":
    main()
