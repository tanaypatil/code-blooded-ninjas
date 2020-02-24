def Rotate(arr, d):
    for i in range(d):
        a = arr[0]
        j = 0
        while j < n-1:
            arr[j] = arr[j+1]
            j += 1
        arr[n-1] = a

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
d=int(input())
Rotate(arr, d)
print(*arr)
