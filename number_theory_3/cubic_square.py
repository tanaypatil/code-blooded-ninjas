"""
Cubic Square
Send Feedback
Varun is learning method of successive squaring so that he can calculate a^b mod m quickly. To give himself practice he wrote many tuples of a, b and m and went to school thinking that he will do it after school.
After school he found that tuples he wrote are modified by his little sister. His sister converted each b into base 3. Varun wrote everything in base 10.
Help Varun to do his excercise.
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



if __name__ == "__main__":
    tc = int(stdin.readline())
    for t in range(tc):
        a, b, m = stdin.readline().strip().split()
        a, m = int(a), int(m)
        b = list(map(int, list(b)))
        b.reverse()
        res = 1
        p = 1
        for i in range(len(b)):
            if b[i] != 0:
                res = (res * power(a, p*b[i], m))%m
            p *= 3
        stdout.write(str(res)+"\n")
        
