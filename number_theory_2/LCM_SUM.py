"""
LCM SUM
Send Feedback
Given n, calculate and print the sum :
LCM(1,n) + LCM(2,n) + .. + LCM(n,n)
where LCM(i,n) denotes the Least Common Multiple of the integers i and n.
"""
## Read input as specified in the question.
## Print output as specified in the question.
from sys import stdin, stdout



if __name__ == "__main__":
    n = int(stdin.readline())
    
    phi = [i for i in range(n+1)]
    for i in range(2, n+1):
        if phi[i] == i:
            j = 2
            phi[i] = i-1
            while i*j <= n:
                phi[i*j] = (phi[i*j]*(i-1))//i
                j += 1
    res = 0

    factors = set()
    for i in range(1, int(n**(0.5))+1):
        if n % i == 0:
            res += i*phi[i]
            if i * i != n:
                res += (n//i)*phi[n//i]
    
    res = (res+1)*n
    res = res//2
    stdout.write(str(res))
            
