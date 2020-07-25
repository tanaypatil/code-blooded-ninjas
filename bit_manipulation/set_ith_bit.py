"""
You are given two integers N and i. You need to make ith bit of binary representation of N to 1 and return the updated N.
"""
## Read input as specified in the question.
## Print output as specified in the question.

def main():
    n, i = map(int, input().split())
    print(n|(1<<i))
    


if __name__ == "__main__":
    main()
