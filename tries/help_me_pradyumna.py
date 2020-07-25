"""
Help Me Pradyumana!
Send Feedback
Pradyumn is tired of using auto - correct feature in his smartphone. He needs to correct his auto - correct more times than the auto - correct corrects him. Pradyumn is thinking to make his own app for mobile which will restrict auto - correct feature, instead it will provide auto - completion. Whenever Pradyumn types factorial, auto - correct changes it to fact. Pradyumn's App will show options such as fact, factorial, factory. Now, he can chose from any of these options. As Pradyumn is busy with his front - end work of his App. He asks you to help him. He said "You will be given set of words(words may repeat too but counted as one only). Now, as user starts the app, he will make queries(in lowercase letters only). So, you have to print all the words of dictionary which have the prefix same as given by user as input. And if no such words are available, add this word to your dictionary." As you know, Pradyumn want this app to be as smart as him :P So, implement a program for him such that he can release it on Fun Store.
"""
from sys import stdin, stdout


class Node:
    def __init__(self):
        self.children = [None]*26
        self.last = False

    def __repr__(self):
        return "$$$$$$$$"
       
    
def getCharIndex(ch):
    return ord(ch)-ord('a')
    
        
def insert(head, string):
    if len(string) == 0:
        return
    temp = head
    for i, s in enumerate(string):
        index = getCharIndex(s)
        try:
            if not temp.children[index]:
            	temp.children[index] = Node()
            temp = temp.children[index]
        except:
            break
    temp.last = True
    
    
def search(head, string):
    if len(string) == 0:
        return -1
    temp = head
    found = True
    for s in string:
        try:
            index = getCharIndex(s)
            if not temp.children[index]:
            	found = False
            	break
            temp = temp.children[index]
        except:
            break
    return temp and temp.last and found


def suggestions_recurse(word, head, words):
    temp = head
    if temp.last:
        words.append(word)
    for i, child in enumerate(temp.children):
        if child:
            suggestions_recurse(word+chr(ord('a')+i), child, words)


def getSuggestions(head, string):
    if len(string) == 0:
        return -1
    temp = head
    
    found = True
    word = ''
    
    for s in string:
        index = getCharIndex(s)
        try:
            if not temp.children[index]:
                found = False
                break
            word += s
            temp = temp.children[index]
        except:
            break
    
    if not found:
        return 0
    
    words = []
    
    suggestions_recurse(word, temp, words)
    return words
    

if __name__ == "__main__":
    n = int(stdin.readline())
    dictionary = []
    head = Node()
    for i in range(n):
        insert(head, stdin.readline())
    q = int(stdin.readline())
    for i in range(q):
        query = stdin.readline()
        res = getSuggestions(head, query)
        if res == 0 or res == -1:
            print("No suggestions")
            insert(head, query)
        else:
            for r in res:
                stdout.write(str(r)+"\n")
    


