"""
3 Cycle
Send Feedback
Given a graph with N vertices (numbered from 1 to N) and Two Lists (U,V) of size M where (U[i],V[i]) and (V[i],U[i]) are connected by an edge , then count the distinct 3-cycles in the graph. A 3-cycle PQR is a cycle in which (P,Q), (Q,R) and (R,P) are connected an edge.
"""
## Read input as specified in the question.
## Print output as specified in the question.

def main():
    n, m = map(int, input().strip().split())
    u = list(map(int, input().strip().split()))
    v = list(map(int, input().strip().split()))
    adj_mat = [[0]*n for _ in range(n)]
    for ui, vi in zip(u, v):
        adj_mat[ui-1][vi-1] = 1
        adj_mat[vi-1][ui-1] = 1
    count = 0
    for i in range(n):
        for j in range(n):
            if i != j and adj_mat[i][j] == 1:
                for k in range(n):
                    if i != k and j != k and adj_mat[j][k] == 1 and adj_mat[i][k] == 1:
                    	count += 1
    print(count//6)



if __name__ == "__main__":
    main()
