"""
Aggressive Cows Problem
Send Feedback
Farmer John has built a new long barn, with N (2 <= N <= 100,000) stalls. The stalls are located along a straight line at positions x1,...,xN (0 <= xi <= 1,000,000,000).
His C (2 <= C <= N) cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, FJ wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?
Input
t – the number of test cases, then t test cases follows. 
* Line 1: Two space-separated integers: N and C
* Lines 2..N+1: Line i+1 contains an integer stall location, xi
Output
For each test case output one integer: the largest minimum distance.
Sample Input :
1
5 3
1
2
8
4
9
Sample Output:
3 
Output details:
FJ can put his 3 cows in the stalls at positions 1, 4 and 8, 
resulting in a minimum distance of 3.
"""


def canArrangeCows(stops, cows, d):
    placed_cows = 0
    for index,stop in enumerate(stops):
        if index == 0:
            placed_cows += 1
            last_stop = 0
        if stops[index] - stops[last_stop] >= d:
            placed_cows += 1
            last_stop = index
        if placed_cows == cows:
            break
    return (placed_cows == cows)
        


def main():
    tc = int(input())
    for t in range(tc):
        n, c = map(int, input().strip().split())
        stops = []
        for i in range(n):
            stops.append(int(input()))
        stops.sort()
        min_d = 0
        max_d = max(stops) - min(stops)
        mid_d = (min_d+max_d)//2 if (min_d + max_d) % 2 == 0 else ((min_d+max_d)//2)+1
        
        while True:
            if mid_d == min_d:
                break
            else:
                if canArrangeCows(stops, c, mid_d):
                    min_d = mid_d
                else:
                    max_d = mid_d - 1
                mid_d = (min_d+max_d)//2 if (min_d + max_d) % 2 == 0 else ((min_d+max_d)//2)+1
        
        print(mid_d)
        
        



if __name__ == "__main__":
    main()
