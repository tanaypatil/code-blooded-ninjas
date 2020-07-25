"""
Kruskal's Algorithm
Send Feedback
Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered from 0 to V-1) and E number of edges.
Find and print the Minimum Spanning Tree (MST) using Kruskal's algorithm.
For printing MST follow the steps -
1. In one line, print an edge which is part of MST in the format -
v1 v2 w
where, v1 and v2 are the vertices of the edge which is included in MST and whose weight is w. And v1 <= v2 i.e. print the smaller vertex first while printing an edge.
2. Print V-1 edges in above format in different lines.
"""
## Read input as specified in the question.
## Print output as specified in the question.
    
def get_parent(i, parent_list):
    if parent_list[i] == i:
        return i
    return get_parent(parent_list[i], parent_list)


def union(v1, v2, parent_list, rank):
    p1 = get_parent(v1, parent_list)
    p2 = get_parent(v2, parent_list)
    
    if rank[p1] < rank[p2]: 
        parent_list[p1] = p2 
    elif rank[p1] > rank[p2]: 
        parent_list[p2] = p1 
    else : 
        parent_list[p2] = p1 
        rank[p1] += 1


def main():
    v, e = map(int, input().strip().split())
    edges = []
    for i in range(e):
        v1, v2, w = map(int, input().strip().split())
        edges.append((v1, v2, w))
    edges = sorted(edges, key=lambda x: x[2])
    count = 0
    parent_list = [i for i in range(v)]
    spanning_edges = []
    rank = [0]*v
    for edge in edges:
        if count >= v-1:
            break
        p1 = get_parent(edge[0], parent_list)
        p2 = get_parent(edge[1], parent_list)
        if p1 != p2:
            spanning_edges.append(edge)
            count += 1
            union(edge[0], edge[1], parent_list, rank)
            
    for edge in spanning_edges:
        if edge[0] < edge[1]:
            print(edge[0], edge[1], edge[2])
        else:
            print(edge[1], edge[0], edge[2])
    



if __name__ == "__main__":
    main()
