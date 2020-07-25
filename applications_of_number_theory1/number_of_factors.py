"""
Number Of Factors
Send Feedback
A number is called n-factorful if it has exactly n distinct prime factors. Given positive integers a, b, and n, your task is to find the number of integers between a and b, inclusive, that are n-factorful. We consider 1 to be 0-factorful.
"""
from sys import stdin, stdout


if __name__ == "__main__":
    sieve = [0]*(10**6+1)
    i = 2
    
    while i <= 10**6:
        if sieve[i] == 0:
            j = 1
            while j*i <= 10**6:
                sieve[j*i] += 1
                j += 1
        i = i+1 if i == 2 else i+2
    
    num_factors = [[0]*(10**6+1) for _ in range(11)]
    
    for i in range(1, 11):
        for j in range(1, 10**6+1):
            num_factors[i][j] = num_factors[i][j-1] + 1 if sieve[j] == i else num_factors[i][j-1]
                
    n = int(input())
    for i in range(n):
        l, r, f = map(int, stdin.readline().strip().split())
        stdout.write(str(num_factors[f][r]-num_factors[f][l-1])+"\n")
