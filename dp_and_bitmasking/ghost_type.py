"""
Ghost Type
Send Feedback
Gengar has got an integer N. Now using his ghostly powers, he can create the permutation from 1 to N of this given number.
Since, he's a special kind of Poke'mon, so he thinks he deserves special permutations. He wants to find the total number of special permutations of length N, consisting of the integers from 1 to N
.

A permutation is called special if it satisfies following condition:
If Ap & Aq == Ap, then p < q, where p and q are two distinct indices of permutation and A is the permutation itself. "&" denotes the bitwise and operation.
Help Gengar in finding the number of such permutations.
"""
from collections import defaultdict
from sys import stdin, stdout


def get_permutations(n, visited_dict, visited, memo, mask):
    if len(visited) == n:
        return 1
    s = 0
    if mask in memo:
        return memo[mask]
    for i in range(1, n+1):
        if not visited_dict[i]:
            f = 0
            for v in visited:
                if i & v == i:
                    f = 1
            if f == 0:
                visited_dict[i] = True
                s += get_permutations(n, visited_dict, visited+[i], memo, mask|1<<i)
                visited_dict[i] = False
    memo[mask] = s
    return s


def main():
    n = int(stdin.readline())
    s = get_permutations(n, defaultdict(bool), [], {}, 0)
    stdout.write(str(s)+"\n")



if __name__ == "__main__":
    main()
