"""
Income On Nth Day
Send Feedback
Daulat Ram is an affluent business man. After demonetization, IT raid was held at his accommodation in which all his money was seized. He is very eager to gain his money back, he started investing in certain ventures and earned out of them. On the first day, his income was Rs. X, followed by Rs. Y on the second day. Daulat Ram observed his growth as a function and wanted to calculate his income on the Nth day.
The function he found out was FN = FN-1 + FN-2 + FN-1×FN-2
Given his income on day 0 and day 1, calculate his income on the Nth day (yeah Its that simple).
"""
import sys


def multiply(A, M):
    MOD = 10**9+6
    v1 = (A[0][0]*M[0][0]%MOD + A[0][1]*M[1][0]%MOD)%MOD
    v2 = (A[0][0]*M[0][1]%MOD + A[0][1]*M[1][1]%MOD)%MOD
    v3 = (A[1][0]*M[0][0]%MOD + A[1][1]*M[1][0]%MOD)%MOD
    v4 = (A[1][0]*M[0][1]%MOD + A[1][1]*M[1][1]%MOD)%MOD

    A[0][0], A[0][1], A[1][0], A[1][1] = v1, v2, v3, v4



def mat_power(A, n):
    if n == 0 or n == 1:
        return

    mat_power(A, n//2)

    multiply(A, A)

    if n % 2 != 0:
        M = [[1, 1], [1, 0]]
        multiply(A, M)



def fib(n):
    A = [[1, 1], [1, 0]]

    if n == 0:
        return 0

    mat_power(A, n-1)
    return A[0][0]%(10**9+7)


def power(a, n):
    MOD = 10**9+7
    if n == 0:
        return 1
    if n == 1:
        return a%MOD
    
    sans = power(a, n//2)%MOD
    ans = (sans * sans)%MOD
    if n % 2 != 0:
        ans = ((a%MOD)*ans)%MOD
        
    return ans%MOD



if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    MOD = 10**9+7
    tc = int(input())
    for t in range(tc):
        f0, f1, n = map(int, input().strip().split())
        if n == 0:
            print(f0)
        elif n == 1:
            print(f1)
        else:
            a, b = 1+f0, 1+f1
            v1 = power(a, fib(n-1))
            v2 = power(b, fib(n))
            v = (v1*v2)%MOD
            v  = (v-1+MOD)%MOD
            print(v)
