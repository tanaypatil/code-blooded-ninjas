# Write your code here

def main():
    t = int(input())
    for i in range(t):
        print(sum(list(map(int,list(input().strip())))))


if __name__ == "__main__":
    main()