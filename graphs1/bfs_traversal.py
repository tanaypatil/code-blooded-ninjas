"""
Code : BFS Traversal
Send Feedback
Given an undirected and disconnected graph G(V, E), print its BFS traversal.
Here you need to consider that you need to print BFS path starting from vertex 0 only.
V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
E is the number of edges present in graph G.
Note : 1. Take graph input in the adjacency matrix.
2. Handle for Disconnected Graphs as well
Input Format :
Line 1: Two Integers V and E (separated by space)
Next 'E' lines, each have two space-separated integers, 'a' and 'b', denoting that there exists an edge between Vertex 'a' and Vertex 'b'.
"""
## Read input as specified in the question.
## Print output as specified in the question.
from sys import stdin, stdout
from queue import Queue


def BFS(i, visited, adj_mat):
    q = Queue()
    q.put(i)
    visited.append(i)
    stdout.write(str(i) + " ")
    while not q.empty():
        vertex = q.get()
        for i in range(len(adj_mat)):
            if i != vertex and i not in visited and adj_mat[vertex][i] == 1:
                q.put(i)
                visited.append(i)
                stdout.write(str(i)+" ")
    


def main():
    v, e = map(int, stdin.readline().strip().split())
    adj_mat = [[0]*v for _ in range(v)]
    for i in range(e):
        v1, v2 = map(int, stdin.readline().strip().split())
        adj_mat[v1][v2] = 1
        adj_mat[v2][v1] = 1
    visited = []
    for i in range(v):
        if i not in visited:
            BFS(i, visited, adj_mat)
        
    



if __name__ == "__main__":
    main()
