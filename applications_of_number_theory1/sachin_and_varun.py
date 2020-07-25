"""
Sachin And Varun Problem
Send Feedback
Varun and you are talking about a movie that you have recently watched while Sachin is busy teaching Number Theory. Sadly, Sachin caught Varun talking to you and asked him to answer his question in order to save himself from punishment. The question says:
Given two weights of a and b units, in how many different ways you can achieve a weight of d units using only the given weights? Any of the given weights can be used any number of times (including 0 number of times).
Since Varun is not able to answer the question, he asked you to help him otherwise he will get punished.
Note: Two ways are considered different if either the number of times a is used or number of times b is used is different in the two ways.
"""

class Triplet:
    def __init__(self):
        self.gcd = 0
        self.x = 0
        self.y = 0
        
        
def gcd(a, b):
    if b == 0:
        return a
    if a < b:
        return gcd(b, a)
    return gcd(b, a%b)
        
        
def extended_euclid(a, b):
    if b == 0:
        a = Triplet()
        a.gcd = a
        a.x = 1
        a.y = 0
        return a
    
    small_ans = extended_euclid(b, a%b)
    ans = Triplet()
    ans.x = small_ans.y
    ans.y = small_ans.x - (a//b)*small_ans.y
    ans.gcd = small_ans.gcd
    return ans


def mod_inverse(a, b):
    ans = extended_euclid(a, b).x
    return (ans%b+b)%b



def main():
    tc = int(input())
    for t in range(tc):
        a, b, d = map(int, input().strip().split())
        g = gcd(a, b)
        
        if d%g:
            print(0)
            continue
        if d == 0:
            print(1)
            continue
        
        A, B, D = a//g, b//g, d//g
        y1 = ((D%A) * mod_inverse(B, A))%A
        fv = D//B
        
        if D < y1*B:
            print(0)
            continue
        
        n = (fv-y1)//A
        print(n+1)



if __name__ == "__main__":
    main()
