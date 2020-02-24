def MissingNumber(arr):
    # Please add your code here
    n = len(arr)
    count = [0]*(n-1)
    for i in arr:
        if count[i] == 1:
            return i
        count[i] += 1

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
ans=MissingNumber(arr)
print(ans)
