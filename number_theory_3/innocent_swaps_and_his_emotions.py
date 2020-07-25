"""
Innocent Swaps and His Emotions
Send Feedback
There are only three phases in Swaps life: Sleep, Play and Study. Also, there are two types of emotions Swaps experiences: Happy and Sad. Each phase of his life brings either kind of emotions.
The sleep and the play phase makes Swaps happy whereas the study phase makes him sad. Quite obvious, isn't it? But we know that life isn't that great, one cannot be happy all the time.
Swaps, being a very sensitive guy, doesn't like to mix his emotions in a particular day. So each day, he is in exactly one of the three phases.
Given N which denotes the number of days and K which denotes the exact number of days Swaps needs to be happy out of these N days, can you tell him in how many ways can he achieve this? Since the output value can be very large, take modulo with 1000000007(10^9+7)
"""
from sys import stdin, stdout


def power(a, n, m):
    if n == 0:
        return 1
    
    sans = power(a, n//2, m)
    ans = (sans * sans)%m
    if n % 2 != 0:
        ans = (a*ans)%m
        
    return ans%m


def fact(n):
    MOD = 10**9+7
    f = 1
    for i in range(1, n+1):
        f = (f * i)%MOD
    return f


def nCr(n, r):
    MOD = 10**9+7
    a = fact(n)
    b = power(fact(n-r), MOD-2, MOD)
    c = power(fact(r), MOD-2, MOD)
    return (a * b * c)%MOD


if __name__ == "__main__":
    tc = int(stdin.readline())
    MOD = 10**9+7
    for t in range(tc):
        n, k = map(int, stdin.readline().strip().split())
        p1 = nCr(n, k)%MOD
        p2 = power(2, k, MOD)
        ans = (p1*p2)%(MOD)
        stdout.write(str(ans) + "\n")
