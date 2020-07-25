"""
INCSEQ
Send Feedback
Given a sequence of N (1 ≤ N ≤ 10,000) integers S1, ..., SN (0 ≤ Si < 100,000), compute the number of increasing subsequences of S with length K (1 ≤ K ≤ 50 and K ≤ N); that is, the number of K-tuples i1, ..., iK such that 1 ≤ i1 < ... < iK ≤ N and Si1 < ... < SiK.
"""
from sys import stdin, stdout


def update(bit, i, j, v, m):
    while j <= m:
        bit[i][j] += v%MOD
        j += j & -j
        
        
def query(bit, i, j):
    s = 0
    while j > 0:
        s += bit[i][j]%MOD
        j -= j & -j
    return s


def main():
    n, k = map(int, stdin.readline().strip().split())
    arr = []
    m = -1
    for i in range(n):
        arr.append(int(stdin.readline()))
        m = max(arr[-1], m)
    bit = [[0]*(m+1) for _ in range(k+1)]
    ans = 0
    for a in arr:
        for i in range(1, k+1):
            p = 1 if i == 1 else query(bit, i-1, a)%MOD
            update(bit, i, a+1, p, m)
            if i == k:
                ans += p%MOD
    stdout.write(str(ans%MOD)+"\n")
    
if __name__ == "__main__":
    MOD = 5*(10**6)
    main()
