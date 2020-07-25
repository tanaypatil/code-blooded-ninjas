"""
Find Prime Numbers From 1 to N
Send Feedback
Given a number N, find number of primes in the range [1,N].
"""
from sys import stdin, stdout
from collections import Counter



if __name__ == "__main__":
    n = int(stdin.readline())
    primes = 0
    sieve = [1]*(n+1)
    sieve[0], sieve[1] = 0, 0
    for i in range(2, int(n**(0.5))+1):
        if sieve[i] == 1:
            for j in range(i, n//i+1):
                sieve[i*j] = 0
    print(Counter(sieve)[1])
            
