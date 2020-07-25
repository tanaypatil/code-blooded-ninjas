"""
Perimeter with conditions
Send Feedback
Aahad gives an array of integers and asks Harshit to find which three elements form a triangle (non-degenerate). The task seems easy to Harshit.
So, Aahad adds some conditions to this task -
1. Find the triangle with maximum perimeter
2. If there are two or more combinations with same value of maximum perimeter, then find the one with the longest side.
3.If there are more than one combinations which satisfy all the above conditions the find with maximum longest minimum side.
"""

def main():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    arr.sort(reverse=True)
    i = 0
    j = 1
    p = -1
    last_ret = (0, 0, 0)
    if n >= 3:
        while j < n-1:
            k = n-1
            while k > j:
                if arr[k] + arr[j] > arr[i]:
                    if arr[i] + arr[j] + arr[k] > p:
                        p = arr[i] + arr[j] + arr[k]
                        last_ret = (arr[i], arr[j], arr[k])
                    elif arr[i] + arr[j] + arr[k] == p:
                        if arr[i] > max(last_ret):
                            last_ret = (arr[i], arr[j], arr[k])
                        elif arr[i] == max(last_ret):
                            if min(arr[i], arr[j], arr[k]) > min(last_ret):
                                last_ret = (arr[i], arr[j], arr[k])
                    else:
                        break
                k -= 1
            i += 1
            j += 1
    if p == -1:
        print(p)
    else:
        ret = [str(last_ret[0]), str(last_ret[1]), str(last_ret[2])]
        ret.sort()
        print(' '.join(ret))
                            

if __name__ == "__main__":
    main()
