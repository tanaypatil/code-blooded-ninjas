"""
Search Engine
Send Feedback
Let us see how search engines work. Consider the following simple auto complete feature. When you type some characters in the text bar, the engine automatically gives best matching options among it's database. Your job is simple. Given an incomplete search text, output the best search result.
Each entry in engine's database has a priority factor attached to it. We consider a result / search suggestion best if it has maximum weight and completes the given incomplete search query. For each query in the input, print the maximum weight of the string in the database, that completes the given incomplete search string. In case no such string exists, print -1.
"""
class Node:
    def __init__(self, weight):
        self.children = [None]*26
        self.weight = 0

    def __repr__(self):
        return "NODE"
        

def charToIndex(ch):
    return ord(ch) - ord("a")
        
        
def insert(head, string, weight):
    if len(string) == 0:
        return
    temp = head
    for i in range(len(string)):
        index = charToIndex(string[i])
        if(index<0 or index>=26):
        	continue
        if not temp.children[index]:
            temp.children[index] = Node(weight)
        if temp.weight < weight:
            temp.weight = weight
        temp = temp.children[index]
        
        
def search_best(head, string):
    if len(string) == 0:
        return -1
    temp = head
    best_weight = -1
    for i in range(len(string)):
        index = charToIndex(string[i])
        if(index<0 or index>=26):
        	continue
        if temp.children[index]:
            best_weight = temp.children[index].weight
            temp = temp.children[index]
        else:
            return -1
    return best_weight



if __name__ == "__main__":
    n, q = map(int, input().strip().split())
    head = Node(-1)
    for i in range(n):
        s, w = input().strip().split()
        insert(head, s, int(w))
    for i in range(q):
        s = input()
        print(search_best(head, s))
