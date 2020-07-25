"""
Nikunj and Donuts
Send Feedback
Nikunj loves donuts, but he also likes to stay fit. He eats n donuts in one sitting, and each donut has a calorie count, ci. After eating a donut with k calories, he must walk at least 2^j x k(where j is the number donuts he has already eaten) miles to maintain his weight.
Given the individual calorie counts for each of the n donuts, find and print a long integer denoting the minimum number of miles Nikunj must walk to maintain his weight. Note that he can eat the donuts in any order.
"""
## Read input as specified in the question.
## Print output as specified in the question.

def main():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    arr.sort(reverse=True)
    m = 0
    for i, a in enumerate(arr):
        m += a*(2**i)
    print(m)


if __name__ == "__main__":
    main()
