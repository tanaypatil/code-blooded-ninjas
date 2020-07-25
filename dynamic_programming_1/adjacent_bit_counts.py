"""
Adjacent Bit Counts
Send Feedback
For a string of n bits x1,x2,x3,...,Xn the adjacent bit count of the string (AdjBC(x)) is given by
X1*X2 + X2*X3 + X3*X4 + ... + Xn-1 * Xn
which counts the number of times a 1 bit is adjacent to another 1 bit. For example:
AdjBC(011101101) = 3
AdjBC(111101101) = 4
AdjBC(010101010) = 0
Write a program which takes as input integers n and k and returns the number of bit strings x of n bits (out of 2ⁿ) that satisfy AdjBC(x) = k. For example, for 5 bit strings, there are 6 ways of getting AdjBC(x) = 2:
11100, 01110, 00111, 10111, 11101, 11011
"""
memo = {}
MOD = 10**9+7


def get_bit_count(n, k, first):
    if n == 1:
        if k == 0:
            return 1
        else:
            return 0
    if k < 0:
        return 0
    global memo
    if (n, k, first) in memo:
        return memo[(n, k, first)]
    if first == 1:
        memo[(n, k, first)] = (get_bit_count(n-1, k-1, 1)%MOD + get_bit_count(n-1, k, 0)%MOD)%MOD
    else:
        memo[(n, k, first)] = (get_bit_count(n-1, k, 0)%MOD + get_bit_count(n-1, k, 1)%MOD)%MOD
    return memo[(n, k, first)]



def main():
    tc = int(input())
    for t in range(tc):
        i, n, k = map(int, input().strip().split())
        print(i, (get_bit_count(n, k, 1)%MOD + get_bit_count(n, k, 0)%MOD)%MOD)
        



if __name__ == "__main__":
    main()
