"""
Given an integer n, using phone keypad find out all the possible strings that can be made using digits of input n.
Return empty string for numbers 0 and 1.
Note : 1. The order of strings are not important.
2. Input and output has already been managed for you. You just have to populate the output array and return the count of elements populated in the output array.
"""

## Read input as specified in the question.
## Print output as specified in the question.

from itertools import product


def convertTuple(tup):
    s = ""
    for i in tup:
        s += ''.join()


def main():
    string = input()
    keypad = {
        "0": "",
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    answer = list(keypad[string[-1]])
    for s in string[-2::-1]:
        a = product(list(keypad[s]), answer)
        ans = []
        for i in a:
            ans.append(''.join(i))
        answer = ans
    for a in answer:
        print(a)

if __name__ == "__main__":
    main()
