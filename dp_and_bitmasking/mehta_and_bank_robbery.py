"""
Mehta And Bank Robbery
Send Feedback
One fine day, when everything was going good, Mehta was fired from his job and had to leave all the work. So, he decided to become a member of gangster squad and start his new career of robbing. Being a novice, mehta was asked to perform a robbery task in which he was given a bag having a capacity W units. So, when he reached the house to be robbed, there lay N items each having particular weight and particular profit associated with it. But, theres a twist associated, He has first 10 primes with him, which he can use atmost once, if he picks any item x, then he can multiply his profit[x] with any of the first 10 primes and then put that item into his bag. Each prime can only be used with one particular item and one item can only have atmost one prime multiplied with its profit. Its not necessary to pick all the items. If he doesnt want to use a prime with any particular item, he can simply add the profit as it is, more specifically, 1*profit[x] for xth item will get added to its total profit, and that he can do with as many items as he wants. He cannot fill his bag more than weight W units. Each item should be picked with its whole weight, i.e it cannot be broken into several other items of lesser weight. So, now to impress his squad, he wishes to maximize the total profit he can achieve by robbing this wealthy house.
"""
## Read input as specified in the question.
## Print output as specified in the question.
from sys import stdin, stdout


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        
    def __repr__(self):
        return "("+str(self.weight)+", "+str(self.value)+")"



if __name__ == "__main__":
    n, W = map(int, stdin.readline().strip().split())
    items = []
    for i in range(n):
        v, w = map(int, stdin.readline().strip().split())
        items.append(Item(w, v))
    items = sorted(items, key=lambda x: x.value)
    dp = [[[0]*(W+1) for _ in range(n+1)] for _ in range(2)]
                
    current = 0
    primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    
    for i in range(1, n+1):
        for j in range(1, W+1):
            dp[0][i][j] = dp[0][i-1][j]
            if j >= items[i-1].weight:
                dp[0][i][j] = max(dp[0][i][j], dp[0][i-1][j-items[i-1].weight]+items[i-1].value)
    
    for p in range(1, 11):
        current = 1-current
        for i in range(1, n+1):
            for j in range(1, W+1):
                dp[current][i][j] = dp[current][i-1][j]
                if j >= items[i-1].weight:
                    dp[current][i][j] = max(dp[current][i][j], dp[current][i-1][j-items[i-1].weight]+items[i-1].value, 
                                           dp[1-current][i-1][j-items[i-1].weight]+items[i-1].value*primes[p])

    stdout.write(str(dp[current][-1][-1])+"\n")
    
