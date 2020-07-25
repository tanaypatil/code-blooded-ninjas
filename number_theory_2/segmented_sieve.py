"""
Segmented Sieve Problem
Send Feedback
In this problem you have to print all primes from given interval.
"""
from sys import stdin, stdout



def print_range_primes(primes, l, u):
    segsieve = [1]*(10**6+1)
    for p in primes:
        first_multiple = (l//p)*p
        if first_multiple < l:
            first_multiple += p
        for i in range(first_multiple, u+1, p):
            segsieve[i-l] = 0
        if first_multiple == p:
            segsieve[first_multiple-l] = 1
    for i in range(u-l+1):
        if segsieve[i] == 1:
            stdout.write(str(i+l)+"\n")


if __name__ == "__main__":
                
    tc = int(stdin.readline())
    n = 10**6
    
    sieve = [1]*(n+1)
    sieve[0], sieve[1] = 0, 0
    for i in range(2, int(n**(0.5))+1):
        if sieve[i] == 1:
            for j in range(i, n//i+1):
                sieve[i*j] = 0
                
    primes = [i for i, a in enumerate(sieve) if a == 1]
    for t in range(tc):
        l, u = map(int, input().strip().split())
        if u <= 10**6:
            for i in range(l, u+1):
                if sieve[i] == 1:
                    stdout.write(str(i)+"\n")
        else:
        	print_range_primes(primes, l, u)
