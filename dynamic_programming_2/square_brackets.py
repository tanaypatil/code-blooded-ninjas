"""
Square Brackets
Send Feedback
You are given:
a positive integer n,
an integer k, 1<=k<=n,
an increasing sequence of k integers 0 < s1 < s2 < ... < sk <= 2n.
What is the number of proper bracket expressions of length 2n with opening brackets appearing in positions s1, s2,...,sk?
Illustration
Several proper bracket expressions:
[[]][[[]][]] 
[[[][]]][][[]]
An improper bracket expression:
[[[][]]][]][[]]
There is exactly one proper expression of length 8 with opening brackets in positions 2, 5 and 7.
Task
Write a program which for each data set from a sequence of several data sets:
1. reads integers n, k and an increasing sequence of k integers from input,
2. computes the number of proper bracket expressions of length 2n with opening brackets appearing at positions s1,s2,...,sk,
3. writes the result to output.
"""
from sys import stdin, stdout


    
def build_expression(n, arr, i, stack, memo):
    if i == 2*n+1:
        if len(stack) == 0:
            return 1
        else:
            return 0
    if (i, str(stack)) in memo:
        return memo[(i, str(stack))]
    opt1 = build_expression(n, arr, i+1, stack + ['['], memo)
    if len(stack) == 0:
        memo[(i, str(stack))] = opt1
        return opt1
    if i in arr:
        ret = opt1
    else:
        ret = opt1 + build_expression(n, arr, i+1, stack[:-1], memo)
    memo[(i, str(stack))] = ret
    return ret



def main():
    tc = int(input())
    for t in range(tc):
        n, k = map(int, stdin.readline().strip().split())
        arr = list(map(int, stdin.readline().strip().split()))
        stack = []
        memo = {}
        if 0 in arr:
            stdout.write(str(build_expression(n, arr, 0, stack, memo))+"\n")
        else:
            stdout.write(str(build_expression(n, arr, 1, stack, memo))+"\n")
    



if __name__ == "__main__":
    main()
