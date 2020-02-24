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
