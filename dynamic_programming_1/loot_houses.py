"""
Loot Houses
Send Feedback
A thief wants to loot houses. He knows the amount of money in each house. He cannot loot two consecutive houses. Find the maximum amount of money he can loot.
"""
def max_sum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    return max(arr[0]+max_sum(arr[2:]), max_sum(arr[1:]))


def max_sum_i(arr):
    res = [0]*len(arr)
    arr.reverse()
    res[0], res[1] = arr[0], arr[1]
    for i in range(2, len(arr)):
        res[i] += max(arr[i] + res[i-2], res[i-1])
    return res[-1]



def main():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    if len(arr) == 1 or len(arr) == 2:
        print(max(arr))
    else:
        print(max_sum_i(arr))



if __name__ == "__main__":
    main()
