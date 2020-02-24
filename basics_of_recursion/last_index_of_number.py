## Read input as specified in the question.
## Print output as specified in the question.
def lastIndex(arr, x, i):
    if len(arr) == 1:
        return i if arr[-1] == x else -1
    if arr[-1] == x:
        return i
    else:
        return lastIndex(arr[:-1], x, i-1)


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    print(lastIndex(arr, x, n-1))
    


if __name__ == "__main__":
    main()