"""
Palindromic Substrings
Send Feedback
Given a string S, count and return the number of substrings of S that are palindrome.
Single length substrings are also palindromes. You just need to calculate the count, not the substrings.
"""
## Read input as specified in the question.
## Print output as specified in the question.



if __name__ == "__main__":
    string = input()
    count = 0
    n = len(string)
    for mid in range(n):
        l, r = mid-1, mid+1
        while 0 <= l < mid and mid < r < n:
            if string[l] != string[r]:
                break
            else:
                count += 1
                l -= 1
                r += 1
        if mid < n-1 and string[mid] == string[mid+1]:
            count += 1
            l, r = mid-1, mid+2
            while 0 <= l < mid and mid+1 < r < n:
                if string[l] != string[r]:
                    break
                else:
                    count += 1
                    l -= 1
                    r += 1
    print(count+n)
