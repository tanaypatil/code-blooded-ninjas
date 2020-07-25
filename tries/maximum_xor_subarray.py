"""
Maximum XOR Subarray
Send Feedback
Given an array of n integers, find subarray whose xor is maximum.
"""

from sys import stdin, stdout


class Node:
    def  __init__(self, data):
        self.data = 0
        self.left = None
        self.right = None
        

def insert(head, x):
    temp = head
    for i in range(31, -1, -1):
        b = x & (1<<i)
        if b:
            if not temp.right:
                temp.right = Node(0)
            temp = temp.right
        else:
            if not temp.left:
                temp.left = Node(0)
            temp = temp.left
    temp.data = x
    
    
def max_xor(head, x):
    temp = head
    for i in range(31, -1, -1):
        b = x & (1<<i)
        if b:
            if temp.left:
                temp = temp.left
            elif temp.right:
                temp = temp.right
        else:
            if temp.right:
                temp = temp.right
            elif temp.left:
                temp = temp.left
    return x ^ temp.data


if __name__ == "__main__":
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split()))
    pre_xor = 0
    max_sub_xor = -float("inf")
    head = Node(pre_xor)
    for a in arr:
        pre_xor = pre_xor ^ a
        insert(head, pre_xor)
        curr_max_xor = max_xor(head, pre_xor)
        max_sub_xor = max(max_sub_xor, curr_max_xor)
    stdout.write(str(max_sub_xor))
