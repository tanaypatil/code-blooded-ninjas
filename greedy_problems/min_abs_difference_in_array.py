"""
Min. Absolute Difference In Array
Send Feedback
Given an integer array A of size N, find and return the minimum absolute difference between any two elements in the array.
We define the absolute difference between two elements ai, and aj (where i != j ) is |ai - aj|.
"""
## Read input as specified in the question.
## Print output as specified in the question.

def main():
    n = int(input())
    a = list(map(int, input().strip().split()))
    a.sort()
    diff = 999999
    for i in range(1, n):
        if abs(a[i]-a[i-1]) < diff:
            diff = abs(a[i]-a[i-1])
    print(diff)


if __name__ == "__main__":
    main()
