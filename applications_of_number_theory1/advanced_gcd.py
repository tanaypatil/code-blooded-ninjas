"""
Advanced GCD
Send Feedback
Varun explained its friend Sanchit the algorithm of Euclides to calculate the GCD of two numbers. Then Sanchit implements the algorithm
int gcd(int a, int b)
{

    if (b==0)
    return a;
    else
    return gcd(b,a%b);
}
and challenges to Varun to calculate gcd of two integers, one is a little integer and other integer has 250 digits.
Your task is to help Varun an efficient code for the challenge of Sanchit.
"""
def gcd(a, b):
    if b == 0:
        return a
    if b > a:
        return gcd(b, a)
    return gcd(b, a%b)



def main():
    tc = int(input())
    for t in range(tc):
        a, b = input().split()
        a = int(a)
        if a == 0:
            print(b)
            continue
        ans = 0
        for s in b:
            ans = (ans*10+int(s))%a
        print(gcd(a, ans))
        
        
        




if __name__ == "__main__":
    main()
