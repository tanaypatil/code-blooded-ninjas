"""
Shil and Wave Sequence
Send Feedback
Given a sequence A1 , A2 , A3 .. AN of length N . Find total number of wave subsequences having length greater than 1.
Wave subsequence of sequence A1 , A2 , A3 .. AN is defined as a set of integers i1 , i2 .. ik such that Ai1 < Ai2 > Ai3 < Ai4 .... or Ai1 > Ai2 < Ai3 > Ai4 .... and i1 < i2 < ...< ik.Two subsequences i1 , i2 .. ik and j1 , j2 .. jm are considered different if k != m or there exists some index l such that il ! = jl
"""
from sys import stdin, stdout


def update(bit, i, j, v, n):
    while i <= n:
        bit[i][j] += v
        i += i & -i


def query(bit, i, j):
    s = 0
    while i > 0:
        s += bit[i][j]
        i -= i & -i
    return s
        
        
def main():
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split()))
    arr = [0] + arr
    m = max(arr)
    bit = [[0, 0, 0] for _ in range(m+2)]
    s = 0
    for i in range(1, n+1):
        a = query(bit, arr[i]-1, 0) + query(bit, arr[i]-1, 2)
        b = query(bit, m, 1) - query(bit, arr[i], 1) + query(bit, m, 2) - query(bit, arr[i], 2)
        update(bit, arr[i], 2, 1, m)
        update(bit, arr[i], 1, a, m)
        update(bit, arr[i], 0, b, m)
        s += a+b
    stdout.write(str(s%(10**9+7))+"\n")



if __name__ == "__main__":
    main()
