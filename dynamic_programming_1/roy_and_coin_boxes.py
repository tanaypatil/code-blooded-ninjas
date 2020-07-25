"""
Roy and Coin Boxes
Send Feedback
Roy has N coin boxes numbered from 1 to N.
Every day he selects two indices [L,R] and adds 1 coin to each coin box starting from L to R (both inclusive).
He does this for M number of days.

After M days, Roy has a query: How many coin boxes have atleast X coins.
He has Q such queries.
"""
from collections import defaultdict, Counter


def main():
    n = int(input())
    m = int(input())
    left_arr = [0]*n
    right_arr = [0]*n
    for i in range(m):
        l, r = map(int, input().strip().split())
        left_arr[l-1] += 1
        right_arr[r-1] += 1
    count_arr = [0]*n
    count_arr[0] = left_arr[0]
    for i in range(1, n):
        count_arr[i] = left_arr[i] - right_arr[i-1] + count_arr[i-1]
    count_dict = Counter(count_arr)
    cum_sum_arr = [0]*n
    i = n-2
    cum_sum_arr[n-1] = count_dict[n]
    while i >= 0:
        cum_sum_arr[i] += count_dict[i+1] + cum_sum_arr[i+1]
        i -= 1
    q = int(input())
    for i in range(q):
        query = int(input())
        print(cum_sum_arr[query-1])


if __name__ == "__main__":
    main()
