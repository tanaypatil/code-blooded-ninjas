"""
KQUERY
Send Feedback
Given a sequence of n numbers a1, a2, ..., an and a number of k- queries. A k-query is a triple (i, j, k) (1 ≤ i ≤ j ≤ n). For each k-query (i, j, k), you have to return the number of elements greater than k in the subsequence ai, ai+1, ..., aj.
"""
from sys import stdin, stdout


class Node:
    def __init__(self):
        self.pos = 0
        self.l = 0
        self.r = 0
        self.val = 0

    def __repr__(self):
        return "( "+str(self.pos)+", "+str(self.l)+", "+str(self.r)+", "+str(self.val)+")"



def update(bit, i, n):
    while i <= n:
        bit[i] += 1
        i += i & -i
        

def query(bit, i):
    s = 0
    while  i > 0:
        s += bit[i]
        i -= i & (-i)
    return s


def solve_query(arr, queries, n, q, ans):
    a = [Node() for _ in range(n+q+1)]
    
    for i in range(1, n+1):
        a[i].val = arr[i-1]
        a[i].l = 0
        a[i].r = i
        a[i].pos = 0
        
    for i in range(n+1, n+q+1):
        a[i].val = queries[i-n-1][2]
        a[i].l = queries[i-n-1][0]
        a[i].r = queries[i-n-1][1]
        a[i].pos = i-n
        
    a = [a[0]] + sorted(a[1:], key=lambda x: (x.val, x.l), reverse=True)
    
    bit = [0]*(n+1)
    
    for i in range(1, n+q+1):
        if a[i].pos != 0:
            count = query(bit, a[i].r) - query(bit, a[i].l-1)
            ans[a[i].pos] = count
        else:
            update(bit, a[i].r, n)

        
def main():
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split()))
    while len(arr) < n:
        arr.append(int(stdin.readline()))
    q = int(stdin.readline())
    queries = []
    for i in range(q):
        l, r, k = map(int, stdin.readline().strip().split())
        queries.append((l, r, k))
    ans = [0]*(q+1)
    solve_query(arr, queries, n, q, ans)
    for a in ans[1:]:
        stdout.write(str(a)+"\n")


        
if __name__ == "__main__":
    main()
