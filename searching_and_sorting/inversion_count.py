"""
Inversion Count
Send Feedback
Let A[0 ... n-1] be an array of n distinct positive integers. If i < j and A[i] > A[j] then the pair (i, j) is called an inversion of A (where i and j are indexes of A). Given an integer array A, your task is to find the number of inversions in A.
Input format :
Line 1 : n, array size
Line 2 : Array elements (separated by space).
Output format :
Count of inversions
Constraints :
1 <= n <= 10^5
1 <= A[i] <= 10^9
Sample Input 1 :
3
3 2 1
Sample Output 1 :
3
Sample Input 2 :
5
2 5 1 3 4
Sample Output 1 :
4
"""


## Read input as specified in the question.
## Print output as specified in the question.
inversion_count = 0

def merge_sort(a):
    global inversion_count
    if len(a) == 1:
        return a
    mid_index = len(a)//2 if len(a) % 2 == 0 else (len(a)//2) + 1 
    left_sorted = merge_sort(a[:mid_index])
    right_sorted = merge_sort(a[mid_index:])
    sorted_array = []
    i=j=0
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] > right_sorted[j]:
            inversion_count += len(left_sorted) - i
            sorted_array.append(right_sorted[j])
            j += 1
        else:
            sorted_array.append(left_sorted[i])
            i += 1
    if j < len(right_sorted):
        while j < len(right_sorted):
            sorted_array.append(right_sorted[j])
            j += 1
    if i < len(left_sorted):
        while i < len(left_sorted):
            sorted_array.append(left_sorted[i])
            i += 1
    return sorted_array
    


def main():
    n = int(input())
    a = list(map(int, input().split()))
    sorted_array = merge_sort(a.copy())
    print(inversion_count)



if __name__ == "__main__":
    main()
