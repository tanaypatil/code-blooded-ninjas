"""
String Search
Send Feedback
Given two strings S and T, write a function to find if T is present as a substring inside S or not. If yes, return the starting index otherwise return -1.
"""
## Read input as specified in the question.
## Print output as specified in the question.
def set_lps(pattern):
    i = 1
    j = 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            lps[i] = j+1
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1

                
def kmp(string, pattern, lps):
    i, j = 0, 0
    while i < len(string) and j < len(pattern):
        if string[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    if j == len(pattern):
        return i-len(pattern)
    else:
        return -1



if __name__ == "__main__":
    string = input()
    pattern = input()
    lps = [0]*len(pattern)
    set_lps(pattern)
    print(kmp(string, pattern, lps))
    
