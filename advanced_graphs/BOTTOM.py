"""
BOTTOM
Send Feedback
We will use the following (standard) definitions from graph theory. Let V be a non-empty and finite set, its elements being called vertices (or nodes). Let E be a subset of the Cartesian product V×V, its elements being called edges. Then G=(V,E) is called a directed graph.

Let n be a positive integer, and let p=(e1,…,en) be a sequence of length n of edges ei∈E such that ei=(vi,vi+1)for a sequence of vertices (v1,…,vn+1). Then p is called a path from vertex v1 to vertex vn+1 in G and we say that vn+1 is reachable from v1, writing (v1→vn+1).

Here are some new definitions. A node v in a graph G=(V,E) is called a sink, if for every node w in G that is reachable from v, v is also reachable from w. The bottom of a graph is the subset of all nodes that are sinks, i.e., bottom(G)={v∈V∣∀w∈V:(v→w)⇒(w→v)}. You have to calculate the bottom of certain graphs.
"""
## Read input as specified in the question.
## Print output as specified in the question.
from sys import stdin
from collections import defaultdict


def visit(i, visited, adj, stack):
    visited[i] = True
    for j in adj[i]:
        if not visited[j]:
            visit(j, visited, adj, stack)
    stack.append(i)
    

def kosaraju(i, visited, adj, cc):
    cc.append(i)
    visited[i] = True
    for j in adj[i]:
        if not visited[j]:
            kosaraju(j, visited, adj, cc)



if __name__ == "__main__":
    while True:
        try:
            v, e = map(int, input().strip().split())
        except:
            break
        adj = defaultdict(list)
        for i in range(e):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        s = stdin.readline()
        visited = defaultdict(bool)
        stack = []
        for i in range(1, v+1):
            if not visited[i]:
                visit(i, visited, adj, stack)
        new_adj = defaultdict(list)
        for k, li in adj.items():
            for l in li:
                new_adj[l].append(k)
        visited = defaultdict(bool)
        components = []
        while len(stack) > 0:
            i = stack.pop()
            cc = []
            if not visited[i]:
                kosaraju(i, visited, new_adj, cc)
                components.append(cc)
        bottoms = []
        for component in components:
            f = 0
            for c in component:
                if f == 1:
                    break
                for a in adj[c]:
                    if a not in component:
                        f = 1
                        break
            if f != 1:
                bottoms.append(component)
        ret = []
        for bottom in bottoms:
            for b in bottom:
                ret.append(b)
        ret.sort()
        for r in ret:
            print(r, end=' ')
        print()
        if s == "0":
            break
