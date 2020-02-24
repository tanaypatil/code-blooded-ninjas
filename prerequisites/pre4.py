
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    a1 = arr[:n//2]
    a2 = arr[-1:(n//2)-1:-1]
    for i, j in zip(a1,a2):
        print((i+j)//10, (i+j)%10)


if __name__ == "__main__":
    main()