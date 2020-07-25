"""
OrderSet - Problem
Send Feedback
In this problem, you have to maintain a dynamic set of numbers which support the two fundamental operations
INSERT(S,x): if x is not in S, insert x into S
DELETE(S,x): if x is in S, delete x from S
and the two type of queries
K-TH(S) : return the k-th smallest element of S
COUNT(S,x): return the number of elements of S smaller than x
"""
from collections import defaultdict
from bisect import bisect_left
from sys import stdin, stdout


def update(bit, i, v, n):
    while i <= n:
        bit[i] += v
        i += i & (-i)
    

def query(bit, i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & (-i)
    return s
        

if __name__ == "__main__":
    n = int(input())
    hmap = {}
    exists = defaultdict(bool)
    bit = [0]*(n+2)
    arr = []
    queries = []
    for t in range(n):
        o, v = stdin.readline().split()
        v = int(v)
        queries.append((o, v))
        if o == "I" and not exists[v]:
            arr.append(v)
            exists[v] = True
    arr.sort()
    arr = [0] + arr
    hmap = {v:k for k, v in enumerate(arr)}
    for o, v in queries:
        # print(bit)
        if o == "I":
            if v in hmap and hmap[v] >= 1 and query(bit, hmap[v]-1) == query(bit, hmap[v]):
                update(bit, hmap[v], 1, n)
        elif o == "D":
            if v in hmap and hmap[v] >= 1 and query(bit, hmap[v]-1) != query(bit, hmap[v]):
                update(bit, hmap[v], -1, n)
        elif o == "K":
            f = 0
            l, r = 0, len(arr)-1
            res = 0
            while r >= l:
                mid = l + (r - l) // 2
                ans = query(bit, mid)
                if ans == v:
                    f = 1
                    res = arr[mid]
                    r = mid-1
                elif ans < v:
                    l = mid+1
                else:
                    r = mid-1
            if f == 0:
                stdout.write("invalid\n")
            else:
                stdout.write(str(res)+"\n")
        else:
            j = bisect_left(arr, v)
            stdout.write(str(query(bit, j-1))+"\n")
