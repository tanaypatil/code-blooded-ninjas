"""
Largest Bitonic Subarray
Send Feedback
You are given an array of positive integers as input. Write a code to return the length of the largest such subsequence in which the values are arranged first in strictly ascending order and then in strictly descending order.
Such a subsequence is known as bitonic subsequence. A purely increasing or purely decreasing subsequence will also be considered as a bitonic sequence with the other part empty.
"""
## Read input as specified in the question.
## Print output as specified in the question.

def main():
    arr = list(map(int, input().strip().split()[1:]))
    count_arr = [(1, 1, 1)]
    for index, a in enumerate(arr[1:], 1):
        i = index-1
        increasing = decreasing = bitonic = 1
        while i >= 0:
            increasing = 1 + count_arr[i][0] if arr[i] < a and 1 + count_arr[i][0] > increasing else increasing
            decreasing = 1 + count_arr[i][1] if arr[i] > a and 1 + count_arr[i][1] > decreasing else decreasing
            bitonic = 1 + count_arr[i][2] if arr[i] > a and 1 + count_arr[i][2] > bitonic else bitonic
            i -= 1
        bitonic = max(increasing, decreasing, bitonic)
        count_arr.append((increasing, decreasing, bitonic))
    bitonics = [x[2] for x in count_arr]
    print(max(bitonics))



if __name__ == "__main__":
    main()
