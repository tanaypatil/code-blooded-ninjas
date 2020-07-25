"""
Problem discussion
Send Feedback
Harshit gave Aahad an array of size N and asked to minimize the difference between the maximum value and minimum value by modifying the array under the condition that each array element either increase or decrease by k(only once).
It seems difficult for Aahad so he asked for your help
"""
def main():
    n, k = map(int, input().strip().split())
    ar = list(map(int, input().strip().split()))
    ar.sort()
    d = ar[-1] - ar[0]
    big = ar[-1] - k
    small = ar[0] + k
    if big < small:
        big, small = small, big
    for a in ar[1:n-1]:
        add = a + k
        sub = a - k
        if add <= big or sub >= small:
            pass
        else:
            if big - sub <= add - small:
                small = sub
            else:
                big = add
                
    print(min(d, big-small))



if __name__ == "__main__":
    main()
