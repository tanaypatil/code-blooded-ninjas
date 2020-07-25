"""
You are given an integer N. You need to return an integer M, in which only one bit is set which at position of lowest set bit of N (from right to left).
"""
## Read input as specified in the question.
## Print output as specified in the question.
def main():
    n = int(input())
    if n == 0:
        print(0)
    elif n % 2 != 0:
        print(1)
    else:
        i = 1
        f = 0
        while n >= (1<<i):
            if n & (1<<i) == (1<<i):
                f = 1
                break
            i += 1
        if f:
            print(1<<i)
        else:
            print(0)

if __name__ == "__main__":
    main()
