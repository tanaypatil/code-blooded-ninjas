def firstIndex(arr, x, i):
    if len(arr) == 1:
        return i if arr[0] == x else -1
    if arr[0] == x:
        return i
    else:
        return firstIndex(arr[1:], x, i+1)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x, 0))
