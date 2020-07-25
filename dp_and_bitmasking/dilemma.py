"""
Dilemma
Send Feedback
Abhishek, a blind man recently bought N binary strings all of equal length .A binary string only contains '0's and '1's . The strings are numbered from 1 to N and all are distinct, but Abhishek can only differentiate between these strings by touching them. In one touch Abhishek can identify one character at a position of a string from the set. Find the minimum number of touches T Abhishek has to make so that he learn that all strings are different .
"""
## Read input as specified in the question.
## Print output as specified in the question.

def get_touches(strings, mask, pos, memo):
    if mask & (mask-1)  == 0:
        return 0
    if pos < 0:
        return 10000
    if (pos, mask) in memo:
        return memo[(pos, mask)]
    mask1, mask2, touches = 0, 0, 0
    for i in range(len(strings)):
        if mask & (1<<i):
            touches += 1
            if strings[i][pos] == '0':
                mask1 = mask1|1<<i
            else:
                mask2 = mask2|1<<i
    ans1 = get_touches(strings, mask1, pos-1, memo) + get_touches(strings, mask2, pos-1, memo) + touches
    ans2 = get_touches(strings, mask, pos-1, memo)
    memo[(pos, mask)] = min(ans1, ans2)
    return min(ans1, ans2)




if __name__ == "__main__":
    n = int(input())
    strings = []
    for i in range(n):
        strings.append(input())
    touches = get_touches(strings, (1<<n)-1, len(strings[0])-1, {})
    print(touches)
    
