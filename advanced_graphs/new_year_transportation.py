"""
New Year Transportation
Send Feedback
New Year Transportation
New Year is coming in Line World! In this world, there are n cells numbered by integers from 1 to n, as a 1 × n board. People live in cells. However, it was hard to move between distinct cells, because of the difficulty of escaping the cell. People wanted to meet people who live in other cells.

 So, user tncks0121 has made a transportation system to move between these cells, to celebrate the New Year. First, he thought of n - 1 positive integers a1, a2, ..., an - 1. For every integer i where 1 ≤ i ≤ n - 1 the condition 1 ≤ ai ≤ n - i holds. Next, he made n - 1 portals, numbered by integers from 1 to n - 1. The i-th (1 ≤ i ≤ n - 1) portal connects cell i and cell (i + ai), and one can travel from cell i to cell (i + ai) using the i-th portal. Unfortunately, one cannot use the portal backwards, which means one cannot move from cell (i + ai) to cell i using the i-th portal. It is easy to see that because of condition 1 ≤ ai ≤ n - i one can't leave the Line World using portals.

Currently, I am standing at cell 1, and I want to go to cell t. However, I don't know whether it is possible to go there. Please determine whether I can go to cell t by only using the construted transportation system.
"""
## Read input as specified in the question.
## Print output as specified in the question.
from collections import defaultdict



def dfs(i, visited, t, arr):
    if i >= len(arr):
        return False
    if i == t-1:
        return True
    visited[i] = True
    next = i+arr[i]
    if not visited[next]:
        if dfs(next, visited, t, arr):
            return True
    return False



if __name__ == "__main__":
    n, t = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    if dfs(0, defaultdict(bool), t, arr):
        print("YES")
    else:
        print("NO")
