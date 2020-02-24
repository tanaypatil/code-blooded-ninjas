from collections import Counter


def differentNames(l):
    c = Counter(l)
    if len(c) == len(l):
        return False
    return {k:v for k,v in c.items() if v > 1}

# Main
names=input().strip().split()
m=differentNames(names)
if m:
    for name in m:
        print(name, m[name])
else:
    print(-1)
