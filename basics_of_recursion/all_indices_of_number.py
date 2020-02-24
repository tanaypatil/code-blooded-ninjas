## Read input as specified in the question.
## Print output as specified in the question.
indexes = []

def allIndexes(arr, x , i):
    if len(arr) == 1:
        if arr[0] == x:
            indexes.append(i)
        return
    if arr[0] == x:
        indexes.append(i)
    allIndexes(arr[1:], x, i+1)


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    allIndexes(arr, x, 0)
    for i in indexes:
        print(i, end=" ")


if __name__ == "__main__":
    main()
