"""
Subset Sum - Problem
Send Feedback
Given a set of n integers, find if a subset of sum k can be formed from the given set. Print Yes or No.
"""
## Read input as specified in the question.
## Print output as specified in the question.

def is_possible(arr, k):
    n = len(arr)
    dp = [[False]*(k+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j] = dp[i-1][j]
            if j >= arr[i-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j-arr[i-1]]
    return dp[-1][-1]



def main():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    if is_possible(arr, k):
        print("Yes")
    else:
        print("No")




if __name__ == "__main__":
    main()
