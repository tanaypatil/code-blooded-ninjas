"""
Given an integer h, find the possible number of balanced binary trees of height h. You just need to return the count of possible binary trees which are balanced.
"""

prime = 1000000007

count_dict = {}

def balancedBTBF(n):
    ''' Return no of balanced BT of height n using Brute Force'''
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if n == 0 or n == 1:
        return 1
    if n in count_dict:
        return count_dict[n]
    count = ((balancedBTBF(n-1)**2)%prime + (2 * balancedBTBF(n-1) * balancedBTBF(n-2))%prime)%prime
    count_dict[n] = count
    return count
    
# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
print(balancedBTBF(n))
