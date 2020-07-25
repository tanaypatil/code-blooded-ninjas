"""
Code : Get Path - DFS
Send Feedback
Given an undirected graph G(V, E) and two vertices v1 and v2(as integers), find and print the path from v1 to v2 (if exists). Print nothing if there is no path between v1 and v2.
Find the path using DFS and print the first path that you encountered.
V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
E is the number of edges present in graph G.
Print the path in reverse order. That is, print v2 first, then intermediate vertices and v1 at last.
"""
## Read input as specified in the question.
## Print output as specified in the question.


def visit(i, visited, adj_mat, v, v2):
    visited.append(i)
    if i == v2:
        return True
    for j in range(v):
        if adj_mat[i][j] == 1 and j not in visited:
            if visit(j, visited, adj_mat, v, v2):
                return True
    visited.pop()
    return False
         
        
def main():
    v, e = map(int, input().strip().split())
    adj_mat = [[0]*v for _ in range(v)]
    for i in range(e):
        v1, v2 = map(int, input().strip().split())
        adj_mat[v1][v2] = 1
        adj_mat[v2][v1] = 1
    v1, v2 = map(int, input().strip().split())
    visited = []
    if visit(v1, visited, adj_mat, v, v2):
    	visited.reverse()
    	for v in visited:
            print(v, end=' ')
        
            
if __name__ == "__main__":
    main()
