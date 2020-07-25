"""
Minimum Number of Chocolates
Send Feedback
Noor is a teacher. She wants to give some chocolates to the students in her class. All the students sit in a line and each of them has a score according to performance. Noor wants to give at least 1 chocolate to each student. She distributes chocolates to them such that If two students sit next to each other then the one with the higher score must get more chocolates. Noor wants to save money, so she wants to minimise the total number of chocolates.
Note that when two students have equal score they are allowed to have different number of chocolates.
"""
## Read input as specified in the question.
## Print output as specified in the question.

def main():
    n = list(map(int,input().strip().split()))
    if len(n) > 1:
        arr = n[1:]
    else:
        arr = list(map(int,input().strip().split()))
    n = n[0]
    arr.reverse()
    dp = [0]*n
    for i in range(n):
        j = i
        c = 0
        if j != n-1:
            while arr[j+1] < arr[j]:
                j += 1
                c += 1
                if j >= n-1:
                    break
        if i == 0:
            dp[i] = c + 1
        else:
            dp[i] = max(c+1, dp[i-1]+1) if arr[i-1] < arr[i] else c+1
    print(sum(dp))
        
            

if __name__ == "__main__":
    main()
