"""
Domino
Dominos are lots of fun. Children like to stand the tiles on their side in long lines. When one domino falls, it knocks down the next one, which knocks down the one after that, all the way down the line.
However, sometimes a domino fails to knock the next one down. In that case, we have to knock it down by hand to get the dominos falling again.
Your task is to determine, given the layout of some domino tiles, the minimum number of dominos that must be knocked down by hand in order for all of the dominos to fall.
"""
## Read input as specified in the question.
## Print output as specified in the question.
import operator
from collections import defaultdict


def visit(i, visited, adj, stack):
    visited[i] = True
    for j in adj[i]:
        if not visited[j]:
            visit(j, visited, adj, stack)
    stack.append(i)


if __name__ == "__main__":
    tc = int(input())
    #print("hello")
    for t in range(tc):
        n, m = map(int, input().strip().split())
        adj = defaultdict(list)
        for i in range(m):
            a, b = map(int, input().strip().split())
            adj[a-1].append(b-1)
        stack = []
        visited = defaultdict(bool)
        for i in range(n):
            if not visited[i]:
                visit(i, visited, adj, stack)
        count = 0
        visited = defaultdict(bool)
        while len(stack) > 0:
            i = stack.pop()
            if not visited[i]:
                count += 1
                visit(i, visited, adj, [])
        print(count)
        
                
