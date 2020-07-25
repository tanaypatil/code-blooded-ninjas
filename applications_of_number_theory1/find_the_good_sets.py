"""
Find the good sets!
Send Feedback
You are given array a consisting of n distinct integers. A set s of numbers is called good if you can rearrange the elements in such a way that each element divides the next element in the order, i.e. 'si' divides 'si + 1', such that i < |s|, where |s| denotes size of set |s|.
Find out number of distinct good sets that you can create using the values of the array. You can use one value only once in a particular set; ie. a set cannot have duplicate values. Two sets are said to be different from each other if there exists an element in one set, which does not exist in the other.
As the answer could be large, print your answer modulo 10^9 + 7.
"""
from collections import defaultdict
from sys import stdin, stdout



if __name__ == "__main__":
    tc = int(stdin.readline())
    MOD = 10**9+7
    for t in range(tc):
        n = int(stdin.readline())
        arr = list(map(int, stdin.readline().strip().split()))
        arr.sort()
        m = max(arr)
        sieve = [0]*(m+1)
        visited = defaultdict(bool)
        s = 0
        for a in arr:
            sieve[a] += 1
            visited[a] = True
        for a in arr:
            j = 2
            s += sieve[a]
            while j*a <= m:
                if visited[j*a]:
                    sieve[j*a] += sieve[a]%MOD
                j += 1
        stdout.write(str(s%MOD)+"\n")
