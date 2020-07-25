"""
Miser Man
Send Feedback
Jack is a wise and miser man. Always tries to save his money.
One day, he wants to go from city A to city B. Between A and B, there are N number of cities(including B and excluding A) and in each city there are M buses numbered from 1 to M. And the fare of each bus is different. Means for all N*M busses, fare (K) may be different or same. Now Jack has to go from city A to city B following these conditions:
1. At every city, he has to change the bus.
2. And he can switch to only those buses which have number either equal or 1 less or 1 greater to the previous.
You are to help Jack to go from A to B by spending the minimum amount of money.
"""

def main():
    n, m = map(int, input().strip().split())
    buses = [list(map(int, input().strip().split())) for _ in range(n)]
    dp = [[0]*m for _ in range(n)]
    for i in range(m):
        dp[0][i] = buses[0][i]
    for i in range(1, n):
        dp[i][0] = buses[i][0] + dp[i-1][0]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = buses[i][j] + min(dp[i-1][:j+1])
    print(min(dp[-1]))




if __name__ == "__main__":
    main()
