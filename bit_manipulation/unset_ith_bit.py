"""
You are given two integers N and i. You need to make ith bit of binary representation of N to 0 and return the updated N.
Counting of bits start from 0 from right to left.
"""
## Read input as specified in the question.
## Print output as specified in the question.

def main():
    n, i = map(int, input().split())
    print(n&(~(1<<i)))


if __name__ == "__main__":
    main()
