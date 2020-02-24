def FindUnique(arr):
    x = arr[0]
    for i in arr[1:]:
        x = x^i
    return x
# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
unique=FindUnique(arr)
print(unique)
