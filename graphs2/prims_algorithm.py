"""
Prim's Algorithm
Send Feedback
Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered from 0 to V-1) and E number of edges.
Find and print the Minimum Spanning Tree (MST) using Prim's algorithm.
For printing MST follow the steps -
1. In one line, print an edge which is part of MST in the format -
v1 v2 w
where, v1 and v2 are the vertices of the edge which is included in MST and whose weight is w. And v1 <= v2 i.e. print the smaller vertex first while printing an edge.
2. Print V-1 edges in above format in different lines.
"""
## Read input as specified in the question.
## Print output as specified in the question.

import sys


def get_min_vertex(visited, weights, v):
    minv = -1
    for i in range(v):
        if visited[i] == False and (minv == -1 or weights[minv] > weights[i]) :
            minv = i
    return minv
    


def prims(edges):
    n = len(edges)
    parents = [None]*n
    weights = [999999999]*n
    visited = [False]*n
    parents[0] = -1
    weights[0] = 0

    for i in range(n-1):
        vertex = get_min_vertex(visited, weights, n)
        visited[vertex] = True
        for j in range(n):
            if edges[vertex][j] != 0 and visited[j] == False:
                if weights[j] > edges[vertex][j]:
                    weights[j] = edges[vertex][j]
                    parents[j] = vertex

    for i in range(1, n):
        if parents[i] < i:
            print(parents[i], i, weights[i])
        else:
            print(i, parents[i], weights[i])


def main():
    v, e = map(int, input().strip().split())
    adj_mat = [[0]*v for _ in range(v)]
    for i in range(e):
        v1, v2, w = map(int, input().strip().split())
        adj_mat[v1][v2] = w
        adj_mat[v2][v1] = w
    prims(adj_mat)
                
    



if __name__ == "__main__":
    main()
