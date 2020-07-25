"""
Count BSTs
Send Feedback
Given an integer N, find and return the count of unique Binary search trees (BSTs) are possible with nodes valued from 1 to N.
Output count can be very large, so return the count modulo 10^9+7.
"""
memo = {}
MOD = 10**9+7


def get_bit_count(n, k, first):
    if n == 1:
        if k == 0:
            return 1
        else:
            return 0
    if k < 0:
        return 0
    global memo
    if (n, k, first) in memo:
        return memo[(n, k, first)]
    if first == 1:
        memo[(n, k, first)] = (get_bit_count(n-1, k-1, 1)%MOD + get_bit_count(n-1, k, 0)%MOD)%MOD
    else:
        memo[(n, k, first)] = (get_bit_count(n-1, k, 0)%MOD + get_bit_count(n-1, k, 1)%MOD)%MOD
    return memo[(n, k, first)]



def main():
    tc = int(input())
    for t in range(tc):
        i, n, k = map(int, input().strip().split())
        print(i, get_bit_count(n, k, 1) + get_bit_count(n, k, 0))
        



if __name__ == "__main__":
    main()
