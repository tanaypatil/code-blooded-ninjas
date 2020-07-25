"""
SUBXOR
Send Feedback
A straightforward question. Given an array of positive integers you have to print the number of subarrays whose XOR is less than K. Subarrays are defined as a sequence of continuous elements Ai, Ai+1, ..., Aj . XOR of a subarray is defined as Ai ^ Ai+1 ^ ... ^ Aj. Symbol ^ is Exclusive Or.
"""
from sys import stdin, stdout


class Node:
    def  __init__(self):
        self.leftLeaf = 0
        self.rightLeaf = 0
        self.left = None
        self.right = None
        # self.parent = None
        

def insert(head, x):
    temp = head
    for i in range(31, -1, -1):
        temp.leaf = 1
        b = (x >> i) & 1
        if b:
            if not temp.right:
                temp.right = Node()
                # temp.right.parent = temp
            temp.rightLeaf += 1
            temp = temp.right
        else:
            if not temp.left:
                temp.left = Node()
                # temp.left.parent = temp
            temp.leftLeaf += 1
            temp = temp.left
    # update(temp)

    
    
def subxor(head, x, k):
    temp = head
    ret = 0
    for i in range(31, -1, -1):
        b = (x >> i) & 1
        kb = (k >> i) & 1
        if temp:
            if b:
                if kb:
                    ret += temp.rightLeaf
                    temp = temp.left
                else:
                    temp = temp.right
            else:
                if kb:
                    ret += temp.leftLeaf
                    temp = temp.right
                else:
                    temp = temp.left      
    return ret
    

def bfs(head):
    temp = head
    q = [temp]
    while len(q) > 0:
        size = len(q)
        for i in range(size):
            node = q[0]
            print(node.leaf, end=' ')
            q = q[1:]
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print()



if __name__ == "__main__":
    tc = int(input())
    for t in range(tc):
        n, k = map(int, input().strip().split())
        arr = list(map(int, input().strip().split()))
        pre_xor = 0
        head = Node()
        head.leaf = 0
        total = 0
        insert(head, pre_xor)
        for a in arr:
            pre_xor = pre_xor ^ a
            total += subxor(head, pre_xor, k)
            insert(head, pre_xor)
        # bfs(head)
        print(total)
            
        
        
