from collections import defaultdict, Counter


def longestConsecutiveIncreasingSequence(l):
    if len(l) == 1:
        return l
    counts = Counter(l)
   

n=int(input())
l=list(int(i) for i in input().strip().split(' '))
final = longestConsecutiveIncreasingSequence(l)
for num in final:
    print(num)
