"""
StairCase Problem
Send Feedback
A child is running up a staircase with n steps and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up to the stairs. You need to return all possible number of ways.
Time complexity of your code should be O(n).
"""

def staircaseDP(n, memo):
    ''' Return possible no of ways to climb n staircase using using Dynamic Prog'''
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n in memo:
        return memo[n]
    memo[n] = staircaseDP(n-1, memo) + staircaseDP(n-2, memo) + staircaseDP(n-3, memo)
    return memo[n]

# Main
n=int(input())
print(staircaseDP(n, {}))
