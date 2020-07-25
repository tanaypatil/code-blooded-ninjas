"""
You are given two integers N and i. You need to clear all bits from MSB to ith bit (start i from right to left) and return the updated N.
Counting of bits starts from 0 from right to left.
"""
## Read input as specified in the question.
## Print output as specified in the question.
def main():
    n, i = map(int, input().split())
    a = 1<<i
    b = a - 1
    c = list(bin(b))[2:]
    d = []
    for i in c:
        if i == 1:
            d.append('0')
        else:
            d.append('1')
    d = ''.join(d)
    d = int(d, 2)
    print(n&d)


if __name__ == "__main__":
    main()
