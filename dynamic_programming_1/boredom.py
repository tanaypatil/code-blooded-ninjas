"""
Boredom
Send Feedback
Gary is bored and wants to play an interesting but tough game . So he figured out a new board game called "destroy the neighbours" . In this game there are N integers on a board. In one move, he can pick any integer x from the board and then all the integers with value x+1 or x-1 gets destroyed .This move will give him x points.
He plays the game until the board becomes empty . But as he want show this game to his friend Steven, he wants to learn techniques to maximise the points to show off . Can you help Gary in finding out the maximum points he receive grab from the game ?
"""
from collections import defaultdict
from sys import stdin

## Read input as specified in the question.
## Print output as specified in the question.
def main():
    n = int(input())
    arr=[]
    for inp in stdin:
        arr += list(map(int, inp.strip().split()))
    counts = defaultdict(int)
    for a in arr:
        counts[a] += 1
    m = max(arr)
    dp = [0, counts[1]]
    for i in range(2, 1001):
        dp.append(max(dp[i-2] + i*counts[i], dp[i-1]))
    print(dp[-1])
        

if __name__ == "__main__":
    main()
