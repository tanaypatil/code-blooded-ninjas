"""
Smallest Super-Sequence
Send Feedback
Given two strings S and T, find and return the length of their smallest super-sequence.
A shortest super sequence of two strings is defined as the shortest possible string containing both strings as subsequences.
"""
import sys


def main():
    string1, string2 = sys.stdin.read().strip().split("\n")
    # string2 = sys.stdin.readline()
    dp = [[0]*(len(string2)+1) for _ in range(len(string1)+1)]
    for i in range(len(string2)+1):
        dp[0][i] = i
    for i in range(len(string1)+1):
        dp[i][0] = i
    for i in range(1, len(string1)+1):
        for j in range(1, len(string2)+1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
    print(dp[-1][-1])



if __name__ == "__main__":
    main()
