"""
Extract Unique characters
Send Feedback
Given a string, you need to remove all the duplicates. That means, the output string should contain each character only once. The respective order of characters should remain same.
Input format :
String S
Output format :
Output String
Constraints :
1 <= Length of S <= 50000
Sample Input 1 :
ababacd
Sample Output 1 :
abcd
Sample Input 2 :
abcde
Sample Output 2 :
abcde
"""


from collections import OrderedDict, Counter


class OrderedCounter(Counter, OrderedDict):
    pass


def uniqueChars(string):
    # Please add your code here
    oc = OrderedCounter(string)
    os = oc.keys()
    return ''.join(os)
    
    

# Main
string = input()
print(uniqueChars(string))
