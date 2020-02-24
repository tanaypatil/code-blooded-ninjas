from collections import defaultdict


def pairSum0(l):
    counts = defaultdict(int)
    for i in l:
        counts[i] += 1
    for i in l:
        if counts[i] > 0 and counts[0-i] > 0:
            for j in range(counts[i]*counts[0-i]):
                if i > 0:
                    print(0-i,i)
                else:
                    print(i,0-i)
            counts[i] = 0
            counts[0-i] = 0

n=int(input())
l=list(int(i) for i in input().strip().split(' '))
pairSum0(l)