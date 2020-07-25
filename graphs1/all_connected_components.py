"""
Code : All connected components
Send Feedback
Given an undirected graph G(V,E), find and print all the connected components of the given graph G.
V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
E is the number of edges present in graph G.
You need to take input in main and create a function which should return all the connected components. And then print them in the main, not inside function.
Print different components in new line. And each component should be printed in increasing order (separated by space). Order of different components doesn't matter.
"""
## Read input as specified in the question.
## Print output as specified in the question.
from sys import stdin, stdout
from queue import Queue


def BFS(i, visited, adj_mat):
    q = Queue()
    q.put(i)
    visited.append(i)
    # stdout.write(str(i) + " ")
    while not q.empty():
        vertex = q.get()
        for i in range(len(adj_mat)):
            if i != vertex and i not in visited and adj_mat[vertex][i] == 1:
                q.put(i)
                visited.append(i)
                # stdout.write(str(i)+" ")
    


def main():
    v, e = map(int, stdin.readline().strip().split())
    adj_mat = [[0]*v for _ in range(v)]
    for i in range(e):
        v1, v2 = map(int, stdin.readline().strip().split())
        adj_mat[v1][v2] = 1
        adj_mat[v2][v1] = 1
    visited = []
    comp = []
    for i in range(v):
        if i not in comp:
            visited = []
            BFS(i, visited, adj_mat)
            visited.sort()
            comp += visited
            v = map(str, visited)
            v = ' '.join(v) + " "
            stdout.write(v + "\n")
    



if __name__ == "__main__":
    main()
