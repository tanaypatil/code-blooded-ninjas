"""
Knapsnack - Problem
Send Feedback
A thief robbing a store and can carry a maximal weight of W into his knapsack. There are N items and ith item weigh wi and is of value vi. What is the maximum value V, that thief can take ?
"""
## Read input as specified in the question.
## Print output as specified in the question.
import sys


def main():
    n = int(sys.stdin.readline())
    w = sys.stdin.read()
    w = w.strip().split("\n")
    w = list(map(int, ' '.join(w).strip().split()))
    weights = w[:n]
    values = w[n:2*n]
    W = w[2*n]
    dp = [0]*(W+1)
    for i in range(1, W+1):
        if weights[0] > i:
            dp[i] = 0
        else:
            dp[i] = values[0]
    t = [0]*(W+1)
    for i in range(1, n):
        temp = t.copy()
        for j in range(1, W+1):
            if j < weights[i]:
                temp[j] = dp[j]
            else:
                temp[j] = max(dp[j], values[i] + dp[j-weights[i]])
        dp = temp.copy()
    sys.stdout.write(str(dp[-1]))


if __name__ == "__main__":
    main()
