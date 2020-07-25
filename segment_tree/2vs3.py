"""
2 vs 3
Send Feedback
The fight for the best number in the globe is going to finally come to an end.The top two contenders for the best number are number 2 and number 3.It's the final the entire world was waiting for. Expectorates from all across the globe came to witness the breath taking finals.
The finals began in an astonishing way.A common problem was set for both of them which included both these number.The problem goes like this.
Given a binary string (that is a string consisting of only 0 and 1). They were supposed to perform two types of query on the string.
Type 0: Given two indices l and r.Print the value of the binary string from l to r modulo 3.

Type 1: Given an index l flip the value of that index if and only if the value at that index is 0.
The problem proved to be a really tough one for both of them.Hours passed by but neither of them could solve the problem.So both of them wants you to solve this problem and then you get the right to choose the best number in the globe.
"""
from sys import stdin, stdout


def build_tree(arr, start, end, tree, treenode):
    if start == end:
        tree[treenode] = arr[start]
        return
    mid = (start + end) // 2
    build_tree(arr, start, mid, tree, 2*treenode+1)
    build_tree(arr, mid+1, end, tree, 2*treenode+2)
    tree[treenode] = tree[2*treenode+1]+tree[2*treenode+2]


def update_tree(arr, tree, start, end, index, treenode):
    if start == end:
        arr[index] = "1" if arr[index] == "0" else arr[index]
        tree[treenode] = "1" if tree[treenode] == "0" else tree[treenode]
        return
    mid = (start + end) // 2
    if start <= index <= mid:
        update_tree(arr, tree, start, mid, index, 2*treenode+1)
    else:
        update_tree(arr, tree, mid+1, end, index, 2*treenode+2)
    tree[treenode] = tree[2*treenode+1]+tree[2*treenode+2]


def query_tree(arr, tree, start, end, s, e, treenode):
    if e < start or s > end:
        return ""

    if start >= s and end <= e:
        return tree[treenode]

    mid = (start + end) // 2
    opt1 = query_tree(arr, tree, start, mid, s, e, 2*treenode+1)
    opt2 = query_tree(arr, tree, mid+1, end, s, e, 2*treenode+2)
    return opt1+opt2
    


def main():
    n = int(stdin.readline())
    arr = list(stdin.readline())
    while len(arr) < n:
        arr += list(stdin.readline())
    arr = arr[:n]
    tree = [""]*(4*n)
    build_tree(arr, 0, n-1, tree, 0)
    queries = int(stdin.readline())
    for q in range(queries):
        query = stdin.readline().split()
        q_type = query[0]
        if q_type == "1":
            # arr[int(query[1])] = "1" if arr[int(query[1])] == "0" else arr[int(query[1])]
            update_tree(arr, tree, 0, n-1, int(query[1]), 0)
        else:
            l, r = int(query[1]), int(query[2])
            st = int(query_tree(arr, tree, 0, n-1, int(query[1]), int(query[2]), 0), 2)%3
            stdout.write(str(st)+"\n")
    


if __name__ == "__main__":
    main()
