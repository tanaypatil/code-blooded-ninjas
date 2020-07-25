"""
Duplicate in array
Send Feedback
Given an array of integers of size n which contains numbers from 0 to n - 2. Each number is present at least once. That is, if n = 5, numbers from 0 to 3 is present in the given array at least once and one number is present twice. You need to find and return that duplicate number present in the array.
Assume, duplicate number is always present in the array.
Input format :
Line 1 : Size of input array
Line 2 : Array elements (separated by space)
Output Format :
Duplicate element
Constraints :
1 <= n <= 10^6
Sample Input:
9
0 7 2 5 4 7 1 3 6
Sample Output:
7
"""


def MissingNumber(arr):
    # Please add your code here
    n = len(arr)
    count = [0]*(n-1)
    for i in arr:
        if count[i] == 1:
            return i
        count[i] += 1

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
ans=MissingNumber(arr)
print(ans)
