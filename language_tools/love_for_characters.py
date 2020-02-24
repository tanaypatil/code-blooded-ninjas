from collections import Counter


def main():
    n = int(input())
    s = input()
    c = Counter(s)
    print(c['a'], end=" ")
    print(c['s'], end=" ")
    print(c['p'], end=" ")



if __name__ == "__main__":
    main()