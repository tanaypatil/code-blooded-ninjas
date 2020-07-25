"""
Distinct Subsequences
Send Feedback
Given a string, count the number of distinct subsequences of it ( including empty subsequence ). For the uninformed, A subsequence of a string is a new string which is formed from the original string by deleting some of the characters without disturbing the relative positions of the remaining characters.
For example, "AGH" is a subsequence of "ABCDEFGH" while "AHG" is not.
"""
def get_subsequences(string):
    last = {}
    n = len(string)
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    for i in range(1, n+1):
        dp[i] = 2 * dp[i-1]
        if string[i-1] in last:
            dp[i] = dp[i] - dp[last[string[i-1]]]
        last[string[i-1]] = i-1
    return dp[-1]


def main():
    tc = int(input())
    for t in range(tc):
        string = input()
        print(get_subsequences(string))


if __name__ == "__main__":
    main()
