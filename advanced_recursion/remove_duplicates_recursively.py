"""
Given a string S, remove consecutive duplicates from it recursively.
"""

# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(s):
    if len(s) >= 2:
        if len(s) == 2:
            if s[0] == s[1]:
                return s[0]
            else:
                return s
        else:
            if s[0] == s[1]:
                i = 1
                while s[i] == s[0]:
                    i += 1
                ret = s[0] + removeConsecutiveDuplicates(s[i:])
            else:
                ret = s[0] + removeConsecutiveDuplicates(s[1:])
            return ret
    else:
        return s

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
