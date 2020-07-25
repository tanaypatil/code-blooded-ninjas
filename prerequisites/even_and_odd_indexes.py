"""
Even and Odd Indexes
Send Feedback
Given an array of integers, print two integer values:
First, the sum of all numbers which are even as well as whose index are even.
Second, the sum of all numbers which are odd as well as whose index are odd.
Print the two integers space separated. (Arrays is 0-indexed)
Input:
Given an integer denoting the size of array.
Next line will have a line containing ‘n’ space separated integers.
Constraints:
1<=n<=10^5
1 <= Ai <= 10^6 
Output:
Two space separated integers denoting even and odd sums respectively.
Sample Input:
5
2 3 5 1 4
Sample Output:
6 4
"""

 
n = int(input())
a = list(input().split())
index = 0
odd_sum = 0
even_sum = 0

for number in a:
    if a[index] % 2 ==0 and index%2 ==0:
        even_sum=even_sum+a[index]
    else if a[index] % 2 !=0 and index % 2!=0:
        odd_sum=odd_sum+a[index]

    index=index+1
    
print(even_sum+" "+odd_sum)
