"""
Vanya and GCD
Send Feedback
Vanya has been studying all day long about sequences and other Complex Mathematical Terms. She thinks she has now become really good at it. So, her friend Vasya decides to test her knowledge and keeps the following challenge it front of her:
Vanya has been given an integer array A of size N. Now, she needs to find the number of increasing sub-sequences of this array with length ≥1 and GCD=1. A sub-sequence of an array is obtained by deleting some (or none) elements and maintaining the relative order of the rest of the elements. As the answer may be large, print it Modulo 109+7
She finds this task really easy, and thinks that you can do it too. Can you?
"""
from collections import defaultdict


MOD = 10**9+7


def gcd(a,b):
    if b == 0:
        return a
    if b == 1:
        return 1
    if b > a:
        return gcd(b, a)
    mod = a%b
    return gcd(b, mod)
    
    

def main():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    count = 0
    dp = [defaultdict(int) for _ in range(n)]
    for i, a in enumerate(arr):
        for j in range(i+1):
            if j == i:
                dp[i][a] = (1+dp[i][a])%MOD   
            else:
                if arr[j] < a:
                    for k, v in dp[j].items(): 
                        dp[i][gcd(a, k)] += v%MOD
        count += dp[i][1]%MOD
    print(count%MOD)
        


if __name__ == "__main__":
    main()
