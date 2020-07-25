"""
Sort an array A using Merge Sort.
Change in the input array itself. So no need to return or print anything.
"""

def mergeSort(arr, start, end):
    if start == end or start > end:
        return 
    mid = (start + end)//2
    mergeSort(arr, start, mid)
    mergeSort(arr, mid+1, end)
    temp = []
    i = start
    j = mid+1
    while i < mid + 1 and j < end+1:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    if i != mid+1:
        while i < mid + 1:
            temp.append(arr[i])
            i += 1
    if j != end+1:
        while j < end + 1:
            temp.append(arr[j])
            j += 1
    for index, a in enumerate(temp):
        arr[index+start] = a

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr, 0, n-1)
for j in arr:
    print(j, end=" ")
