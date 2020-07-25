"""
Sum Array
Send Feedback
Given a 2-d square matrix of order ‘n’, find the sum of elements of both diagonals and all boundaries elements. Boundary elements refer to the elements present on all the four boundaries of matrix.
Input:
First line will have a single integer ‘n’ denoting the order of matrix.
Next ‘n’ lines will have ‘n’ space separated integers each denoting the elements of matrix.
Constraints:
1<=n<=100
Output:
Print a single integer denoting the sum.
Sample input:
3
1 2 3
4 5 6
7 8 9
Sample Output:
45
"""



n = int(input())
matrix = []
s = 0
for i in range(n):
    matrix.append(list(map(int, input().split())))
for index1,i in enumerate(matrix):
    for index2,j in enumerate(i):
        if index1 == 0 or index1 == n-1:
            s += j
        elif index2 == 0 or index2 == n-1:
            s += j
        elif index1 == index2 or abs(index1+index2) == n-1:
            s += j
print(s)