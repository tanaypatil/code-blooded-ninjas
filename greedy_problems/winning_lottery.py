"""
Winning Lottery
Send Feedback
Harshit knows by his resources that this time the winning lottery number is the smallest number whose sum of the digits is S and the number of digits is D. You have to help Harshit and print the winning lottery number.
"""
def main():
    s, d = map(int, input().strip().split())
    arr = [0]*d
    arr[0] = 1
    i = len(arr) - 1
    while i > 0:
        if sum(arr) + 9 <= s:
            arr[i] = 9
        else:
            arr[i] = s-sum(arr)
        if sum(arr) == s:
            break
        i -= 1
    if 1 < sum(arr)-s <= 9:
        arr[0] = sum(arr) - s
    arrs = [str(x) for x in arr]
    print(''.join(arrs))
            
        


if __name__ == "__main__":
    main()
