"""
GCD
Send Feedback
Calculate and return GCD of two given numbers x and y. Numbers are within range of Integer.
"""
## Read input as specified in the question.
## Print output as specified in the question.
def gcd(a,b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a%b)


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(gcd(a, b))
