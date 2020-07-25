"""
Edit Distance - Problem
Send Feedback
Given two strings s and t of lengths m and n respectively, find the Edit Distance between the strings. Edit Distance of two strings is minimum number of steps required to make one string equal to other. In order to do so you can perform following three operations only :
1. Delete a character

2. Replace a character with another one

3. Insert a character
"""
## Read input as specified in the question.
## Print output as specified in the question.

def main():
    s1 = input()
    s2 = input()
    dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    for i in range(len(s2)+1):
        dp[0][i] = i
    for i in range(1, len(s1)+1):
        dp[i][0] = i
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    print(dp[-1][-1])



if __name__ == "__main__":
    main()
