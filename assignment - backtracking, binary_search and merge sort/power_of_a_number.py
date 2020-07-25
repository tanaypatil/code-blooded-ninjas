"""
Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.
"""

## Read input as specified in the question.
## Print output as specified in the question.

def main():
    n, p = map(int, input().split())
    print(n**p)


if __name__ == "__main__":
    main()
