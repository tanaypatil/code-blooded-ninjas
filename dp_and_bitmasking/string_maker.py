"""
String Maker
Send Feedback
According to Ancient Ninjas , string making is an art form . There are various methods of string making , one of them uses previously generated strings to make the new one . Suppose you have two strings A and B , to generate a new string C , you can pick a subsequence of characters from A and a subsequence of characters from B and then merge these two subsequences to form the new string.
Though while merging the two subsequences you can not change the relative order of individual subsequences. What this means is - suppose there two characters Ai and Aj in the subsequence chosen from A , where i < j , then after merging if i acquires position k and j acquires p then k<p should be true and the same apply for subsequence from C.
Given string A , B , C can you count the number of ways to form string C from the two strings A and B by the method described above. Two ways are different if any of the chosen subsequence is different .
As the answer could be large so return it after modulo 10^9+7
"""
## Read input as specified in the question.
## Print output as specified in the question.
from sys import stdin, stdout
from collections import defaultdict


def get_ways(a, b, c, x, y, z, memo):
    if z < 0:
        return 1
    if (x, y, z) in memo:
        return memo[(x, y, z)]
    s = 0
    for i in range(x, -1, -1):
        if a[i] == c[z]:
            s += get_ways(a, b, c, i-1, y, z-1, memo)
    for j in range(y, -1, -1):
        if b[j] == c[z]:
            s += get_ways(a, b, c, x, j-1, z-1, memo)
    memo[(x, y, z)] = s
    return s


def main():
    a = input()
    b = input()
    c = input()
    n1, n2, n3 = len(a), len(b), len(c)
    s = get_ways(a, b, c, n1-1, n2-1, n3-1, {})
    print(s%(10**9+7))
    

if __name__ == "__main__":
    main()
