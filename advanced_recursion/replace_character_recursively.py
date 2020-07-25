"""
Given an input string S and two characters c1 and c2, you need to replace every occurrence of character c1 with character c2 in the given string.
"""

## Read input as specified in the question.
## Print output as specified in the question.
        
def main():
    s = input()
    c1, c2 = input().strip().split()
    print(s.replace(c1, c2))


if __name__ == "__main__":
    main()

    
    
"""
## Read input as specified in the question.
## Print output as specified in the question.

def replaceChar(s, c1, c2):
    print(s)
    if len(s) >= 1:
        if len(s) > 1:
            if s[0] == c1:
                return c2 + replaceChar(s[1:], c1, c2)
            else:
                return s[0] + replaceChar(s[1:], c1, c2)
        else:
            print("here")
            if s[0] == c1:
                print("here1")
                return c2
            else:
                print("here2")
                return s[0]

        
def main():
    s = input()
    c1, c2 = input().strip().split()
    s = replaceChar(s, c1, c2)
    print(s)


if __name__ == "__main__":
    main()

"""
