"""
Sort an array A using Quick Sort.
Change in the input array itself. So no need to return or print anything.
"""
def partition(arr, start, end):
    pivot = arr[end]
    p_index = start
    for i in range(start, end+1):
        if arr[i] < pivot:
            arr[p_index], arr[i] = arr[i], arr[p_index]
            p_index += 1
    arr[p_index], arr[end] = arr[end], arr[p_index]
    return p_index
    

def quickSort(arr, start, end):
    if start >= end:
        return
    p_index = partition(arr, start, end)
    quickSort(arr, start, p_index-1)
    quickSort(arr, p_index+1, end)

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n-1)
print(*arr)
