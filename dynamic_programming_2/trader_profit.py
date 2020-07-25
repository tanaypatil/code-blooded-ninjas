"""
Trader Profit
Send Feedback
Mike is a stock trader and makes a profit by buying and selling stocks. He buys a stock at a lower price and sells it at a higher price to book a profit. He has come to know the stock prices of a particular stock for n upcoming days in future and wants to calculate the maximum profit by doing the right transactions (single transaction = buying + selling). Can you help him maximize his profit?
Note: A transaction starts after the previous transaction has ended. Two transactions can't overlap or run in parallel.
The stock prices are given in the form of an array A for n days.
Given the stock prices and a positive integer k, find and print the maximum profit Mike can make in at most k transactions.
"""
def main():
    tc = int(input())
    for t in range(tc):
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        dp = [[0]*n for _ in range(k+1)]
        for i in range(1, k+1):
            dp[i][0] = 0
        for i in range(1, k+1):
            maxdiff = -arr[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], arr[j] + maxdiff)
                maxdiff = max(maxdiff, dp[i-1][j] - arr[j])
        print(dp[-1][-1])


if __name__ == "__main__":
    main()
