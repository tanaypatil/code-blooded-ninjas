"""
All Indices of Number
Send Feedback
Given an array of length N and an integer x, you need to find all the indexes where x is present in the input array. Save all the indexes in an array (in increasing order).
Do this recursively. Indexing in the array starts from 0.
Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Line 3 : Integer x
Output Format :
indexes where x is present in the array (separated by space)
Constraints :
1 <= N <= 10^3
Sample Input :
5
9 8 10 8 8
8
Sample Output :
1 3 4
"""


## Read input as specified in the question.
## Print output as specified in the question.
indexes = []

def allIndexes(arr, x , i):
    if len(arr) == 1:
        if arr[0] == x:
            indexes.append(i)
        return
    if arr[0] == x:
        indexes.append(i)
    allIndexes(arr[1:], x, i+1)


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    allIndexes(arr, x, 0)
    for i in indexes:
        print(i, end=" ")


if __name__ == "__main__":
    main()
