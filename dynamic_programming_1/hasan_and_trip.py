"""
Hasan and Trip
Send Feedback
Hasan has finally finished his final exams and he decided to go in a trip among cities in Syria.
There are N cities in Syria and they are numbered from 1 to N, each city has coordinates on plane, i-th city is in (Xi, Yi).
Hasan is in first city and he wants to visit some cities by his car in the trip but the final destination should be N-th city and the sequence of cities he will visit should be increasing in index (i.e. if he is in city i he can move to city j if and only if i < j ).
Visiting i-th city will increase Hasan's happiness by Fi units (including first and last cities), also Hasan doesn't like traveling too much, so his happiness will decrease by total distance traveled by him.
Help Hasan by choosing a sequence of cities to visit which maximizes his happiness.
"""
from collections import defaultdict

## Read input as specified in the question.
## Print output as specified in the question.

def get_maximum_happiness(arr):
    dp = [-999999]*len(arr)
    dp[0] = arr[0][2]
    for i in range(1, len(arr)):
        for j in range(i):
            opt1 = dp[i]
            opt2 = dp[j] - ((arr[i][0]-arr[j][0])**2 + (arr[i][1]-arr[j][1])**2)**(0.5)
            dp[i] = max(opt1, opt2)
        dp[i] += arr[i][2]
    return dp[-1]

There are N cities in Syria and they are numbered from        
    


def main():
    n = int(input())
    arr = []
    for i in range(n):
        x, y, f = map(int, input().strip().split())
        arr.append((x, y, f))
    res_str = str(round(get_maximum_happiness(arr), 6))
    ez = ""
    if len(res_str.split('.')[-1]) < 6:
        for i in range(6-len(res_str.split('.')[-1])):
            ez += "0"
    print(res_str+ez)
    
    
        

if __name__ == "__main__":
    main()
