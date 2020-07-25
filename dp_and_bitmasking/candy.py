"""
Candy
Send Feedback
Gary is a teacher at XYZ school. To reward his N students he bought a packet of N candies all with different flavours. But the problem is some students like certain flavour while some doesn't. Now Gary wants to know the number of ways he can distribute these N candies to his N students such that every student gets exactly one candy he likes.
"""
## Read input as specified in the question.
## Print output as specified in the question.
from collections import defaultdict
from sys import stdin, stdout


def findWays(adj, mask, n, i, memo):
    if i >= n:
        if mask == (1<<n) - 1:
            return 1
        return 0
    if (i, mask) in memo:
        return memo[(i, mask)]
    s = 0
    for j in adj[i]:
        if not (mask&1<<(n-1-j)):	
            s += findWays(adj, mask|1<<(n-1-j), n, i+1, memo)
    memo[(i, mask)] = s
    return s




def main():
    n = int(stdin.readline())
    adj = defaultdict(list)
    for i in range(n):
        for j, a in enumerate(stdin.readline().split()):
            if a == "1":
                adj[i].append(int(j))
    memo = {}
    ways = findWays(adj, 0, n, 0, memo)
    stdout.write(str(ways)+"\n")



if __name__ == "__main__":
    main()
