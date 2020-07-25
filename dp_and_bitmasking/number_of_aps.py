"""
Number of APs
Send Feedback
Given an array of n positive integers. The task is to count the number of Arithmetic Progression subsequences in the array. As the answer could be very large, output it modulo 100001.
Note: Empty sequence or single element sequence is Arithmetic Progression.
"""
## Read input as specified in the question.
## Print output as specified in the question.
import sys
from collections import defaultdict, Counter


if __name__ == "__main__":
    inp = sys.stdin.readline().split()
    n = int(inp[0])
    arr = list(map(int, inp[1:]))
    while len(arr) < n:
        arr += list(map(int, sys.stdin.readline().split()))
    gdict = {i:defaultdict(int) for i in range(n)}
    counts = defaultdict(int)
    visited = set()
    for k, v in gdict.items():
        l = len(visited)
        visited.add(arr[k])
        if len(visited) == l:
            v[0] = 0
        else:
            v[0] = 1
        counts[arr[k]] += 1
    for i in range(n-1, -1, -1):
        j = i+1
        while j < n:
            diff = arr[j]-arr[i]
            gdict[i][diff] += 1 + gdict[j][diff]
            j += 1
    s = 0
    for emap in gdict.values():
        s += sum(emap.values())
    for a, c in counts.items():
        if c > 1:
            s += (c-1)
    print((1+s)%100001)
