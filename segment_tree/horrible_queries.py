"""
Horrible Queries
Send Feedback
World is getting more evil and it's getting tougher to get into the Evil League of Evil. Since the legendary Bad Horse has retired, now you have to correctly answer the evil questions of Dr. Horrible, who has a PhD in horribleness (but not in Computer Science). You are given an array of N elements, which are initially all 0. After that you will be given C commands. They are -
0 p q v - you have to add v to all numbers in the range of p to q (inclusive), where p and q are two indexes of the array.

1 p q - output a line containing a single integer which is the sum of all the array elements between p and q (inclusive)
"""
from sys import stdin, stdout


def increment_tree(tree, lazy_tree, start, end, s, e, value, treenode):
    if start > end:
        return
    
    if lazy_tree[treenode] != 0:
        tree[treenode] += lazy_tree[treenode]*(end-start+1)
        if start != end:
            lazy_tree[2*treenode+1] += lazy_tree[treenode]
            lazy_tree[2*treenode+2] += lazy_tree[treenode]
        lazy_tree[treenode] = 0
    
    if e < start or s > end:
        return

    if start >= s and e >= end:
        tree[treenode] += value*(end-start+1)
        if start != end:
            lazy_tree[2*treenode+1] += value
            lazy_tree[2*treenode+2] += value
        return
    
    mid = (start + end) // 2
    increment_tree(tree, lazy_tree, start, mid, s, e, value, 2*treenode+1)
    increment_tree(tree, lazy_tree, mid+1, end, s, e, value, 2*treenode+2)
    tree[treenode] = tree[2*treenode+1] + tree[2*treenode+2]



def query_tree(tree, lazy_tree, start, end, s, e, treenode):

    if lazy_tree[treenode] != 0:
        tree[treenode] += lazy_tree[treenode]*(end-start+1)
        if start != end:
            lazy_tree[2*treenode+1] += lazy_tree[treenode]
            lazy_tree[2*treenode+2] += lazy_tree[treenode]
        lazy_tree[treenode] = 0

    if e < start or s > end:
        return 0

    if start >= s and end <= e:
        return tree[treenode]

    mid = (start + end) // 2
    opt1 = query_tree(tree, lazy_tree, start, mid, s, e, 2*treenode+1)
    opt2 = query_tree(tree, lazy_tree, mid+1, end, s, e, 2*treenode+2)
    return opt1+opt2


def main():
    tc = int(stdin.readline())
    for t in range(tc):
        n, queries = map(int, stdin.readline().strip().split())
        arr = [0]*n
        tree = [0]*(4*n)
        lazy_tree = [0]*(4*n)
        for q in range(queries):
            query = list(map(int, stdin.readline().strip().split()))
            if query[0] == 0:
                l, r, v = query[1], query[2], query[3]
                increment_tree(tree, lazy_tree, 0, n-1, l-1, r-1, v, 0)
            else:
                l, r = query[1], query[2]
                ret = query_tree(tree, lazy_tree, 0, n-1, l-1, r-1, 0)
                stdout.write(str(ret)+"\n")


if __name__ == "__main__":
    main()
