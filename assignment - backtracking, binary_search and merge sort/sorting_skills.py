"""
There is a company named James Peterson & Co. The company has ‘n’ employees. The employees have skills from 0 to n-1. All the employees have distinct skills. The manager of James Peterson & Co. wants to sort the employees on the basis of their skills in ascending order. He is only allowed to swap two employees which are adjacent to each other. He is given the skills of employees in an array of size ‘n’. He can swap the skills as long as the absolute difference between their skills is 1. You need to help the manager out and tell whether it is possible to sort the skills of employees or not.
"""

def mergeSort(arr, start, end):
    if start == end:
        return
    else:
        mid = (start+end)//2
        mergeSort(arr, start, mid)
        mergeSort(arr, mid+1, end)
        if arr[mid] - arr[mid+1] == 1:
            arr[mid], arr[mid+1] = arr[mid+1], arr[mid]
        
        
def main():
    tc = int(input())
    for t in range(tc):
        n = int(input())
        arr = list(map(int, input().split()))
        sorted_arr = sorted(arr)
        mergeSort(arr, 0, len(arr)-1)
        if arr == sorted_arr:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
