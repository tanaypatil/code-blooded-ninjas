"""
Strange order
Send Feedback
Given an integer n . Initially you have permutation p of size n : p[i] = i . To build new array a from p following steps are done while permutation p is not empty:
Choose maximum existing element in p and define it as x ; Choose all such y in p that gcd ( x , y ) ≠ 1 ; Add all chosen numbers into array a in decreasing order and remove them from permutation. Your task is to find a after p became empty.
Note: gcd ( a , b ) is the greatest common divisor of integers a and b .
"""
from collections import defaultdict
from sys import stdin, stdout


if __name__ == "__main__":
    n = int(stdin.readline())
    sieve = [i for i in range(n+1)]
    for i in range(2, n):
        if sieve[i] == i:
            j = 2
            while i*j <= n:
                sieve[i*j] = min(sieve[i*j], i)
                j += 1
    
    visited = defaultdict(bool)
    ret = []
    for i in range(n, 0, -1):
        if not visited[i]:
            visited[i] = True
            temp = [i]
            lpd = sieve[i]
            p = i
            while True:
                a = i
                a -= lpd
                while a > 0:
                    if not visited[a]:
                        temp.append(a)
                        visited[a] = True
                    a -= lpd
                if sieve[p] == p:
                    break
                while p > lpd and p % lpd == 0:
                    p = p // lpd
                lpd = sieve[p]
            ret += sorted(temp, reverse=True)
    print(*ret, " ")
