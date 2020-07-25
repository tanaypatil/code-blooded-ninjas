"""
Minimum Count
Send Feedback
Given an integer N, find and return the count of minimum numbers, sum of whose squares is equal to N.
That is, if N is 4, then we can represent it as : {1^2 + 1^2 + 1^2 + 1^2} and {2^2}. Output will be 1, as 1 is the minimum count of numbers required.
"""
## Read input as specified in the question.
## Print output as specified in the question.
memo = {1: 1, 2: 2, 3: 3}


def get_num_ways(n, arr):
    global memo
    if n < 0:
        return 0
    if n in memo:
        return memo[n]
    if len(arr) == 0:
        return 0
    if (n**(0.5))**2 == int(n**(0.5))**2:
        ret = 1
    else:
        take_j = get_num_ways(n-arr[0]**2, arr)
        remove_j = get_num_ways(n, arr[1:])
    memo[n] = ret
    return ret


def main():
    n = int(input())
    print(get_num_ways(n, [x for x in range(int(n**(0.5)))]))


if __name__ == "__main__":
    main()
