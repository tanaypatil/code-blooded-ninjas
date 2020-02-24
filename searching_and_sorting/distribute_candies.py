# Write your code here
def ifPossible(arr,m,k):
    count = 0
    for index,a in enumerate(arr):
        count += a//m
    return count >= k


def main():
    tc = int(input())
    for t in range(tc): 
        n, k = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        a.sort()
        lower_limit = a[n-k] if n > k else 0
        upper_limit = a[-1]
        middle_limit = (lower_limit + upper_limit)//2
        while lower_limit < middle_limit:
            if ifPossible(a,middle_limit,k):
                lower_limit = middle_limit
            else:
                upper_limit = middle_limit
            middle_limit = (lower_limit + upper_limit)//2
        print(lower_limit)
    



if __name__ == "__main__":
    main()