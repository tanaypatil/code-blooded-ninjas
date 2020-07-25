"""
GCD Extreme
Send Feedback
Given the value of N, you will have to find the value of G. The meaning of G is given in the following code
G=0;
for(i = 1 ; i < N ; i++)
   for(j = i+1 ; j <= N ; j++) 
       G+=gcd(i,j);
Here gcd() is a function that finds the greatest common divisor of the two input numbers.
"""
from sys import stdin, stdout



if __name__ == "__main__":
    arr = []
    MAX = 0
    while True:
        n = int(stdin.readline())
        if n == 0:
            break
        arr.append(n)
        MAX = max(MAX, n)
    MAX += 1
        
    
    phi = [i for i in range(MAX)]
    for i in range(2, MAX):
        if phi[i] == i:
            j = 2
            phi[i] = i-1
            while i*j < MAX:
                phi[i*j] = (phi[i*j]*(i-1))//i
                j += 1
    
    res = [0]*MAX
    for i in range(MAX):
        for j in range(2, MAX):
            if i*j >= MAX:
                break
            res[i*j] += i * phi[j]

    for i in range(2, MAX):
        res[i] += res[i-1]
    for a in arr:
        stdout.write(str(res[a])+"\n")
            
