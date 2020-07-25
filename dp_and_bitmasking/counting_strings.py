"""
Counting Strings
Send Feedback
Given a string 's' consisting of upper case alphabets, i.e. from 'A' to 'Z'. Your task is to find how many strings 't' with length equal to that of 's', also consisting of upper case alphabets are there satisfying the following conditions:
-> String 't' is lexicographical larger than string 's'.
-> When you write both 's' and 't' in the reverse order, 't' is still lexicographical larger than 's'.
Find out number of such strings 't'. As the answer could be very large, take modulo 10^9 + 7.
"""
## Read input as specified in the question.
## Print output as specified in the question.

if __name__ == "__main__":
    string = list(input())
    su, p = 0, 0
    MOD = 10**9+7
    for s in string:
        su += ((p+1)%MOD*(ord("Z")-ord(s))%MOD)%MOD
        p = ((p*26)%MOD + (ord("Z")-ord(s))%MOD)%MOD
    print(su%MOD)
