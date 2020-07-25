"""
Fibonacci Sum
Send Feedback
The fibonacci sequence is defined by the following relation:
 F(0) = 0
 F(1) = 1
 F(N) = F(N - 1) + F(N - 2), N >= 2
Your task is very simple. Given two non-negative integers N and M (N <= M), you have to calculate and return the sum (F(N) + F(N + 1) + ... + F(M)) mod 1000000007.
"""
def multiply(A, M):
    v1 = A[0][0]*M[0][0] + A[0][1]*M[1][0]
    v2 = A[0][0]*M[0][1] + A[0][1]*M[1][1]
    v3 = A[1][0]*M[0][0] + A[1][1]*M[1][0]
    v4 = A[1][0]*M[0][1] + A[1][1]*M[1][1]

    A[0][0], A[0][1], A[1][0], A[1][1] = v1, v2, v3, v4



def power(A, n):
    if n == 0 or n == 1:
        return

    power(A, n//2)

    multiply(A, A)

    if n % 2 != 0:
        M = [[1, 1], [1, 0]]
        multiply(A, M)



def fib(n):
    A = [[1, 1], [1, 0]]

    if n == 0:
        return 0

    power(A, n-1)
    print(A)
    return A



if __name__ == "__main__":
    l = int(input())
    u = int(input())
    A = [[1, 1], [1, 0]]
    if l > 2:
        power(A, l-1)
        res = A[0][0]
    else:
        l += 2
        res = 2
    M = [[1, 1], [1, 0]]
    for i in range(u-l):
        multiply(A, M)
        res += A[0][0]
    print(res%(10**9+7))
