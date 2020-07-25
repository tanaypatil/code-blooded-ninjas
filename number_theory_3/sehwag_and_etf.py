"""
Sehwag And ETF
Send Feedback
Sehwag has been solving a lot of mathematical problems recently. He was learning ETF (Euler Totient Function) and found the topic quite interesting. So, he tried solving a question on ETF. He will be given two numbers L and R. He has to find the probability that the ETF of a number in the range [L, R] is divisible by a number K.
"""


def get_phi(value, primes):
    res = val
    for i in range(len(primes)):
        while val % primes[i] == 0:
            val /= primes[i]
            res = (res//primes[i]) * (primes[i]-1)
    if val > 1:
        res = res//val*(val-1)
    return res



if __name__ == "__main__":
    pr = [1]*(2**20)
    pr[0], pr[1] = 0, 0
    for i in range(2, 10**6+1):
        if pr[i]:
            j = 2
            while i * j <= 10**6:
                pr[i*j] = 0
                j += 1
                
    vec = [0]*(2**20)
    for i in range(2, 10**6+1):
        if not pr[i]:
            continue
        bnd = l//(i*i)
        if l % i > 0:
            bnd += i
        for j in range(bnd, r+1, i):
            vec[j-l] = i
    
    tc = int(input())
    for t in range(tc):
        l, r, k = map(int, input().strip().split())
        ans = 0
        for i in range(l, r+1):
            Q = get_phi(i, vec[:i-l])
            if Q%k == 0:
                ans += 1
        
        print("{:.6f}".format(round(ans/(r-l+1), 6)))
