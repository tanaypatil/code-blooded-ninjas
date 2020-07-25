"""
Divisors Of Factorial
Send Feedback
Given a number, find the total number of divisors of the factorial of the number.
Since the answer can be very large, print answer modulo 10^9+7.
"""
from collections import Counter


def num_primes(n):
    primes = 0
    sieve = [1]*(n+1)
    sieve[0], sieve[1] = 0, 0
    for i in range(2, int(n**(0.5))+1):
        if sieve[i] == 1:
            for j in range(i, n//i+1):
                sieve[i*j] = 0
    nums = []
    for i,s in enumerate(sieve):
        if s == 1:
            nums.append(i)
    return Counter(sieve)[1], nums


    
def num_divisors(n):
    MOD = 10**9+7
    limit, primes = num_primes(n)
    ans = 1
    for i in range(limit):
        j = 1
        s = 0
        while n//(primes[i]**j) > 0:
            s += (n//(primes[i]**j))%MOD
            j += 1
        ans *= (1+s)%MOD
    return ans%MOD
    
    

def main():
    tc = int(input())
    for t in range(tc):
        n = int(input())
        if n == 0 or n == 1:
            print(1)
            continue
        print(num_divisors(n))



if __name__ == "__main__":
    main()
