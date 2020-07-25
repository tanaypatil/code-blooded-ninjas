"""
PARTY - Problem
Send Feedback
You just received another bill which you cannot pay because you lack the money.
Unfortunately, this is not the first time to happen, and now you decide to investigate the cause of your constant monetary shortness. The reason is quite obvious: the lion's share of your money routinely disappears at the entrance of party localities.
You make up your mind to solve the problem where it arises, namely at the parties themselves. You introduce a limit for your party budget and try to have the most possible fun with regard to this limit.
You inquire beforehand about the entrance fee to each party and estimate how much fun you might have there. The list is readily compiled, but how do you actually pick the parties that give you the most fun and do not exceed your budget?
Write a program which finds this optimal set of parties that offer the most fun. Keep in mind that your budget need not necessarily be reached exactly. Achieve the highest possible fun level, and do not spend more money than is absolutely necessary.
"""
from sys import stdin, stdout


def knapsack(weights, values, W, n):
    dp = [[0]*(W+1) for _ in range(n+1)]
    cost = 0
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif j < weights[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                opt1 = dp[i-1][j]
                opt2 = values[i-1] + dp[i-1][j-weights[i-1]]
                dp[i][j] = max(opt1, opt2)
    res = dp[-1][-1]
    w = W 
    for i in range(0,W+1):
        if res==dp[n][i]:
            cost = i
            break
    # for i in range(n, 0, -1):
    #     if res <= 0 or w <= 0: 
    #     #     break
    #     # if res == dp[i-1][w]: 
    #     #     continue
    #     # else:
    #     #     cost += weights[i-1]
    #     #     res = res - values[i-1] 
    #     #     w = w - weights[i-1]
            
    return cost, dp[-1][-1]


def main():
    while True:
        # W, n = [int(i) for i in input().strip().split()]
        W, n = map(int, stdin.readline().strip().split())
        if W == 0 and n == 0:
            break
        weights = []
        values = []
        for i in range(n):
            # w, v = [int(i) for i in input().strip().split()]
            w, v = map(int, stdin.readline().strip().split())
            weights.append(w)
            values.append(v)
        res = knapsack(weights, values, W, n)
        # print(res[0], res[1])
        res_str = str(res[0]) + " " + str(res[1]) + "\n"
        stdout.write(res_str)
        s = input()


if __name__ == "__main__":
    main()
