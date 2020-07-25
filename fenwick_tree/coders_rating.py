"""
Coder's Rating
Send Feedback
Some of the more elite (and not-so-elite) coders around take part in a certain unnamed programming contest. In said contest, there are multiple types of competitions. Here, we consider the Open and High School competition types. For each type, each competitor receives a rating, an integer between 1 and 100000, inclusive. A coder's rating is based upon his or her level of performance in matches and is calculated using a complicated formula which, thankfully, you will not be asked to implement.
Although the Open and High School ratings for a coder who has participated in both competition types lately are usually close, this is not always the case. In particular, High School matches are more about speed, since many coders are able to solve all the problems, whereas Open matches require more thinking and there is a steeper curve in terms of problem difficulty.
"""
import operator


def update(bit, i):
    i += 1
    while i <= 1000001:
        bit[i] += 1
        i += (i & (-i))
        
        
def query(bit, i):
    i += 1
    s = 0
    while i > 0:
        s += bit[i]
        i -= (i & (-i))
    return s


if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        x, y = map(int, input().strip().split())
        arr.append((i, x, y))
    arr = sorted(arr, key=operator.itemgetter(1, 2))
    bit = [0]*(1000001)
    ans = [0]*n
    i = 0
    while i < n:
        end_index = i
        while end_index < n and arr[i][1] == arr[end_index][1] and arr[i][2] == arr[end_index][2]:
            end_index += 1
        for j in range(i, end_index):
            ans[arr[j][0]] += query(bit, arr[j][2])
        for j in range(i, end_index):
            update(bit, arr[j][2])
        i = end_index

    for a in ans:
        print(a)
    
    
    
