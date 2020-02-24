
def main():
    n, required_sum = map(int, input().split())
    arr = list(map(int, input().split()))
    start_index = -1
    end_index = -1
    s = 0
    f = 0
    while end_index < n:
        if s > required_sum:
            if start_index == end_index:
                s -= arr[start_index]
                start_index = end_index = end_index + 1
                s += arr[end_index]
            else:
                s -= arr[start_index]
                start_index += 1
        elif s < required_sum:
            if start_index == -1:
                start_index += 1
            end_index += 1
            if end_index < n:
                s += arr[end_index]
        else:
            f = 1
            break
    if f == 1:
        print("true")
        for i in range(start_index, end_index+1):
            print(arr[i], end=" ")
    else:
        print("false")
    


if __name__ == "__main__":
    main()