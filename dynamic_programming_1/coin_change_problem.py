"""
Coin Change Problem
Send Feedback
You are given an infinite supply of coins of each of denominations D = {D0, D1, D2, D3, ...... Dn-1}. You need to figure out the total number of ways W, in which you can make change for Value V using coins of denominations D.
Note : Return 0, if change isn't possible.
"""
## Read input as specified in the question.
## Print output as specified in the question.
def coinChange(arr, v, memo):
    if v == 0:
        return 1
    if v < 0:
        return 0
    if len(arr) == 0:
        return 0
    if (len(arr), v) in memo:
        return memo[(len(arr), v)]
    take_denomination = coinChange(arr, v-arr[0], memo)
    remove_denomination = coinChange(arr[1:], v, memo)
    memo[len(arr), v] = take_denomination + remove_denomination
    return memo[len(arr), v]


def main():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    v = int(input())
    print(coinChange(arr, v, {}))


if __name__ == "__main__":
    main()
