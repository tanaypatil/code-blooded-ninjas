"""
Kingdom Of Monkeys
Send Feedback
This is the story in Zimbo, the kingdom officially made for monkeys. Our Code Monk visited Zimbo and declared open a challenge in the kingdom, thus spoke to all the monkeys :

You all have to make teams and go on a hunt for Bananas. The team that returns with the highest number of Bananas will be rewarded with as many gold coins as the number of Bananas with them. May the force be with you!
Given there are N monkeys in the kingdom. Each monkey who wants to team up with another monkey has to perform a ritual. Given total M rituals are performed. Each ritual teams up two monkeys. If Monkeys A and B teamed up and Monkeys B and C teamed up, then Monkeys A and C are also in the same team.

You are given an array A where Ai is the number of bananas i'th monkey gathers.

Find out the number of gold coins that our Monk should set aside for the prize.
"""
## Read input as specified in the question.
## Print output as specified in the question.
import sys
from collections import defaultdict


def dfs(i, visited, cc):
    visited[i] = True
    cc.append(i)
    for j in adj[i]:
        if not visited[j]:
            dfs(j, visited, cc)



if __name__ == "__main__":
    sys.setrecursionlimit(50000)
    tc = int(input())
    for t in range(tc):
        n, m = map(int, input().strip().split())
        adj = defaultdict(list)
        for i in range(m):
            x, y = map(int, input().strip().split())
            adj[x-1].append(y-1)
            adj[y-1].append(x-1)
        values = list(map(int, input().strip().split()))
        visited = defaultdict(bool)
        m = 0
        for i in range(n):
            if not visited[i]:
                cc = []
                dfs(i, visited, cc)
                m = max(m, sum([values[j] for j in cc]))
        print(m)
