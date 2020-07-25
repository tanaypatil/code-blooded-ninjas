"""
Distinct Query Problem
Send Feedback
Given a sequence of n numbers a1, a2, ..., an and a number of d-queries. A d-query is a pair (i, j) (1 ≤ i ≤ j ≤ n). For each d-query (i, j), you have to return the number of distinct elements in the subsequence ai, ai+1, ..., aj.
"""
import operator
from sys import stdout, stdin


def update(i, bit, v, n):
    while i <= n:
        bit[i] += v
        i += i & (-i)
        

def query(i, bit):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & (-i)
    return s


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split()))
    while(len(arr)!=n):
        a=list(map(int,stdin.readline().split()))
        arr=arr+a
    arr = [0] + arr
    q = int(input())
    queries = []
    m = -1
    for i in range(q):
        s, e = map(int, stdin.readline().strip().split())
        queries.append((s, e, i))
    queries = sorted(queries, key=operator.itemgetter(1))
    last_visited = [-1]*1000001
    k = 0
    bit = [0]*(n+2)
    ans = [0]*q
    f = 0
    total = 0
    for i in range(1, n+1):
        if f == 1:
            break
        if last_visited[arr[i]] != -1:
            last_index = last_visited[arr[i]]
            update(last_index, bit, -1, n)
        else:
            total += 1
        update(i, bit, 1, n)
        last_visited[arr[i]] = i
        while i == queries[k][1]:
            s, e, index = queries[k]
            ans[index] = total-query(s-1, bit)
            k += 1
            if k == q:
                f = 1
                break
    for a in ans:
        stdout.write(str(a)+"\n")
