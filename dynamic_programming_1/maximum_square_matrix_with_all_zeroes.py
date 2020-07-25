"""
Maximum Square Matrix With All Zeros
Send Feedback
Given a n*m matrix which contains only 0s and 1s, find out the size of maximum square sub-matrix with all 0s. You need to return the size of square with all 0s.
"""
## Read input as specified in the question.
## Print output as specified in the question.

def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i])
    print("------")



def main():
    n, m = map(int, input().strip().split())
    arr = [list(map(int, input().strip().split())) for _ in range(n)]
    dp_arr = [[0]*m for _ in range(n)]
    for row in range(n):
        dp_arr[row][0] = 1 if arr[row][0] == 0 else 0
    for col in range(m):
        dp_arr[0][col] = 1 if arr[0][col] == 0 else 0
    m1 = max(dp_arr[0])
    m2 = max([dp_arr[row][0] for row in range(n)])
    max_s = max(m1, m2)
    for row in range(1, n):
        for col in range(1, m):
            dp_arr[row][col] = min(dp_arr[row-1][col-1], dp_arr[row-1][col], dp_arr[row][col-1]) + 1 if arr[row][col] == 0 else 0
            max_s = max(max_s, dp_arr[row][col])
    print(max_s)
            



if __name__ == "__main__":
    main()
