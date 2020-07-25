"""
You are given an integer Ni. You need to make first set bit of binary representation of N to 0 and return the updated N.
Counting of bits start from 0 from right to left.
"""
## Read input as specified in the question.
## Print output as specified in the question.

def main():
    n = int(input())
    i = 0
    if n == 0:
        print(0)
        return
    f = 1
    while n >= (1<<i):
        if (n&(1<<i)) == (1<<i):
            f = 1
            break
        i += 1
    if f == 1:
        print(n&(~(1<<i)))
    else:
        print(0)

if __name__ == "__main__":
    main()
