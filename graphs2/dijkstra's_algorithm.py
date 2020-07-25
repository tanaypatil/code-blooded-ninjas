"""
Dijkstra's Algorithm
Send Feedback
Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered from 0 to V-1) and E number of edges.
Find and print the shortest distance from the source vertex (i.e. Vertex 0) to all other vertices (including source vertex also) using Dijkstra's Algorithm.
Print the ith vertex number and the distance from source in one line separated by space. Print different vertices in different lines.
"""
## Read input as specified in the question.
## Print output as specified in the question.

from collections import defaultdict


def minDistance(dist, visited, n): 
    minv = 9223372036854775807
    min_index = 0
    for v in range(n): 
        if dist[v] < minv and visited[v] == False: 
            minv = dist[v] 
            min_index = v 
  
    return min_index 


def dijkstra(adj_mat): 
    infinity = 9223372036854775807
    n = len(adj_mat)
    dist = [infinity] * n 
    dist[0] = 0
    visited = [False] * n 
  
    for cout in range(n):
        u = minDistance(dist, visited, n)
        visited[u] = True 
        for v in range(n): 
            if adj_mat[u][v] > 0 and visited[v] == False and dist[v] > dist[u] + adj_mat[u][v]: 
                dist[v] = dist[u] + adj_mat[u][v]
    for i in range(n):
        print(i, dist[i])
  
    


def main():
    v, e = map(int, input().strip().split())
    edges = defaultdict(list)
    adj_mat = [[0]*v for _ in range(v)]
    for i in range(e):
        v1, v2, w = map(int, input().strip().split())
        adj_mat[v1][v2] = w
        adj_mat[v2][v1] = w
    dijkstra(adj_mat)
                
    



if __name__ == "__main__":
    main()
