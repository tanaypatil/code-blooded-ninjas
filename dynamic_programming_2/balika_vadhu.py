"""
Balika Vadhu- Problem
Send Feedback
Anandi and Jagya were getting married again when they have achieved proper age. Dadi Sa invited Alok Nath to do the kanyadaan and give blessings. Alok Nath has 2 blessings. Each bessing is in the form of a string consisting of lowercase charaters(a-z) only. But he can give only one blessing of K length because some priest told him to do so. Thus he decides to generate a blessing using the other two blessings. While doing this he wants to ensure that happiness brought into their life by his blessing is maximum.
The generated blessing is a common subsequence of length K of the two blessings he has. Happiness of the blessing he generates is calculated by the sum of ASCII values of characters in the blessing and he wants the happiness to be maximum. If he is not able to generate a common subsequence of length K then the happiness is 0 (zero). Alok Nath comes to you and asks you to find the maximum happiness that can be generated by the two blessings he has.
"""
INT_MIN = -9999999999


def get_max_happiness(s1, s2, k):
    dp = [[[0]*(k+1) for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    for i in range(len(s1)+1):
        dp[i][0][0] = 0
        for z in range(1, k+1):
            dp[i][0][z] = INT_MIN
    for i in range(len(s2)+1):
        dp[0][i][0] = 0
        for z in range(1, k+1):
            dp[0][i][z] = INT_MIN
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            dp[i][j][0] = 0
            if s1[i-1] == s2[j-1]:
                for z in range(1, k+1):                
                    dp[i][j][z] = max(dp[i-1][j-1][z-1] + ord(s1[i-1]), dp[i-1][j][z], dp[i][j-1][z])
            else:
                for z in range(1, k+1):
                    dp[i][j][z] = max(dp[i-1][j][z], dp[i][j-1][z])
    if dp[-1][-1][-1] < 0:
        return 0
    else:
        return dp[-1][-1][-1]
                    
        


def main():
    tc = int(input())
    for t in range(tc):
        s1 = input()
        s2 = input()
        k = int(input())
        print(get_max_happiness(s1, s2, k))




if __name__ == "__main__":
    main()
