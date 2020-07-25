"""
Counting Even/Odd
Send Feedback
Ashu and Shanu are best buddies. One day Shanu gives Ashu a problem to test his intelligence.He gives him an array of N natural numbers and asks him to solve the following queries:-
Query 0 :- modify the element present at index i to x.
Query 1:- count the number of even numbers in range l to r inclusive.
Query 2:- count the number of odd numbers in range l to r inclusive.
"""
from sys import stdin, stdout


def build_tree(arr, start, end, tree, treenode):
    if start == end:
        tree[treenode] = [1, 0] if arr[start] % 2 != 0 else [0, 1]
        return
    mid = (start + end) // 2
    build_tree(arr, start, mid, tree, 2*treenode+1)
    build_tree(arr, mid+1, end, tree, 2*treenode+2)
    tree[treenode] = [tree[2*treenode+1][0] + tree[2*treenode+2][0], tree[2*treenode+1][1] + tree[2*treenode+2][1]]


def update_tree(arr, tree, start, end, index, value, treenode):
    if start == end:
        arr[index] = value
        tree[treenode] = [1, 0] if arr[start] % 2 != 0 else [0, 1]
        return
    mid = (start + end) // 2
    if start <= index <= mid:
        update_tree(arr, tree, start, mid, index, value, 2*treenode+1)
    else:
        update_tree(arr, tree, mid+1, end, index, value, 2*treenode+2)
    tree[treenode] = [tree[2*treenode+1][0] + tree[2*treenode+2][0], tree[2*treenode+1][1] + tree[2*treenode+2][1]]


def query_tree(arr, tree, start, end, s, e, treenode):
    if e < start or s > end:
        return [0, 0]

    if start >= s and end <= e:
        return tree[treenode]

    mid = (start + end) // 2
    opt1 = query_tree(arr, tree, start, mid, s, e, 2*treenode+1)
    opt2 = query_tree(arr, tree, mid+1, end, s, e, 2*treenode+2)
    return [opt1[0] + opt2[0], opt1[1] + opt2[1]]
    


def main():
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split()))
    queries = int(stdin.readline())
    tree = [0]*(4*n)
    build_tree(arr, 0, n-1, tree, 0)
    for q in range(queries):
        query = stdin.readline().split()
        q_type = query[0]
        if q_type == "0":
            update_tree(arr, tree, 0, n-1, int(query[1])-1, int(query[2]), 0)
        elif q_type == "1":
            ret = query_tree(arr, tree, 0, n-1, int(query[1])-1, int(query[2])-1, 0)[1]
            stdout.write(str(ret) + "\n")
        else:
            ret = query_tree(arr, tree, 0, n-1, int(query[1])-1, int(query[2])-1, 0)[0]
            stdout.write(str(ret) + "\n")
    

if __name__ == "__main__":
    main()
