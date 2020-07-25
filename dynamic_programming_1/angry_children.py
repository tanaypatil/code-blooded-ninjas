"""
Angry Children
Send Feedback
Bill Gates is on one of his philanthropic journeys to a village in Utopia. He has N packets of candies and would like to distribute one packet to each of the K children in the village (each packet may contain different number of candies). To avoid a fight between the children, he would like to pick K out of N packets such that the unfairness is minimized.
Suppose the K packets have (x1, x2, x3,....xk) candies in them, where xi denotes the number of candies in the ith packet, then we define unfairness as
unfairness=0;
for(i=0;i<n;i++)
for(j=0;j<n;j++)
    unfairness+=abs(xi-xj)
abs(x) denotes absolute value of x.
"""
def get_min_unfairness(arr, k):
    target = 0
    s = arr[0]
    for i in range(1, k):
        target += i*arr[i] - s
        s += arr[i]
    min_unfairness = target
    for i in range(k, len(arr)):
        unfairness = target - 2*(s-arr[i-k]) + (k-1)*(arr[i-k]+arr[i])
        if unfairness < min_unfairness:
            min_unfairness = unfairness
        s = s-arr[i-k]+arr[i]
        target = unfairness
    return min_unfairness



def main():
    n = int(input())
    k = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    if k == 1:
        print(max(arr))
        return
    if n == 2 and k == 2:
        print(abs(arr[0]-arr[1]))
        return
    if k > n:
        print(0)
        return
    arr.sort()
    print(get_min_unfairness(arr, k))


if __name__ == "__main__":
    main()
