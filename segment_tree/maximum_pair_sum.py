"""
Maximum Pair Sum
Send Feedback
You are given a sequence A[1], A[2], ..., A[N], ( 0 ≤ A[i] ≤ 10^8 , 2 ≤ N ≤ 10^5 ). There are two types of operations and they are defined as follows:
Update:
This will be indicated in the input by a 'U' followed by space and then two integers i and x.
U i x, 1 ≤ i ≤ N, and x, 0 ≤ x ≤ 10^8.
This operation sets the value of A[i] to x.
Query:
This will be indicated in the input by a 'Q' followed by a single space and then two integers i and j.
Q x y, 1 ≤ x < y ≤ N.
You must find i and j such that x ≤ i, j ≤ y and i != j, such that the sum A[i]+A[j] is maximized. Print the sum A[i]+A[j].
"""
from sys import stdin, stdout


def build_tree(arr, start, end, tree, treenode):
    if start == end:
        tree[treenode] = [arr[start], arr[start], 0]
        return
    mid = (start + end) // 2
    build_tree(arr, start, mid, tree, 2*treenode+1)
    build_tree(arr, mid+1, end, tree, 2*treenode+2)
    opt1 = tree[2*treenode+1][0]
    opt2 = tree[2*treenode+2][0]
    opt3 = tree[2*treenode+1][1] + tree[2*treenode+2][1]
    opt4 = tree[2*treenode+1][2] + tree[2*treenode+2][2]
    opt5 = tree[2*treenode+1][1] + tree[2*treenode+2][2]
    opt6 = tree[2*treenode+1][2] + tree[2*treenode+2][1]
    max_opt = max(opt1, opt2, opt3, opt4, opt5, opt6)
    if max_opt == opt1:
        tree[treenode] = [max_opt, tree[2*treenode+1][1], tree[2*treenode+1][2]]
    elif max_opt == opt2:
        tree[treenode] = [max_opt, tree[2*treenode+2][1], tree[2*treenode+2][2]]
    elif max_opt == opt3:
        tree[treenode] = [max_opt, tree[2*treenode+1][1], tree[2*treenode+2][1]]
    elif max_opt == opt4:
        tree[treenode] = [max_opt, tree[2*treenode+1][2], tree[2*treenode+2][2]]
    elif max_opt == opt5:
        tree[treenode] = [max_opt, tree[2*treenode+1][1], tree[2*treenode+2][2]]
    else:
        tree[treenode] = [max_opt, tree[2*treenode+1][2], tree[2*treenode+2][1]]


def update_tree(arr, tree, start, end, index, value, treenode):
    if start == end:
        arr[index] = value
        tree[treenode] = [value, value, 0]
        return
    mid = (start + end) // 2
    if start <= index <= mid:
        update_tree(arr, tree, start, mid, index, value, 2*treenode+1)
    else:
        update_tree(arr, tree, mid+1, end, index, value, 2*treenode+2)
    opt1 = tree[2*treenode+1][0]
    opt2 = tree[2*treenode+2][0]
    opt3 = tree[2*treenode+1][1] + tree[2*treenode+2][1]
    opt4 = tree[2*treenode+1][2] + tree[2*treenode+2][2]
    opt5 = tree[2*treenode+1][1] + tree[2*treenode+2][2]
    opt6 = tree[2*treenode+1][2] + tree[2*treenode+2][1]
    max_opt = max(opt1, opt2, opt3, opt4, opt5, opt6)
    if max_opt == opt1:
        tree[treenode] = [max_opt, tree[2*treenode+1][1], tree[2*treenode+1][2]]
    elif max_opt == opt2:
        tree[treenode] = [max_opt, tree[2*treenode+2][1], tree[2*treenode+2][2]]
    elif max_opt == opt3:
        tree[treenode] = [max_opt, tree[2*treenode+1][1], tree[2*treenode+2][1]]
    elif max_opt == opt4:
        tree[treenode] = [max_opt, tree[2*treenode+1][2], tree[2*treenode+2][2]]
    elif max_opt == opt5:
        tree[treenode] = [max_opt, tree[2*treenode+1][1], tree[2*treenode+2][2]]
    else:
        tree[treenode] = [max_opt, tree[2*treenode+1][2], tree[2*treenode+2][1]]


def query_tree(arr, tree, start, end, s, e, treenode):
    if e < start or s > end:
        return [0, 0, 0]

    if start >= s and end <= e:
        return tree[treenode]

    mid = (start + end) // 2
    option1 = query_tree(arr, tree, start, mid, s, e, 2*treenode+1)
    option2 = query_tree(arr, tree, mid+1, end, s, e, 2*treenode+2)
    opt1 = option1[0]
    opt2 = option2[0]
    opt3 = option1[1] + option2[1]
    opt4 = option1[2] + option2[2]
    opt5 = option1[1] + option2[2]
    opt6 = option1[2] + option2[1]
    max_opt = max(opt1, opt2, opt3, opt4, opt5, opt6)
    if max_opt == opt1:
        return [max_opt, option1[1], option1[2]]
    elif max_opt == opt2:
        return [max_opt, option2[1], option2[2]]
    elif max_opt == opt3:
        return [max_opt, option1[1], option2[1]]
    elif max_opt == opt4:
        return [max_opt, option1[2], option2[2]]
    elif max_opt == opt5:
        return [max_opt, option1[1], option2[2]]
    else:
        return [max_opt, option1[2], option2[1]]
    


def main():
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split()))
    tree = [0]*(4*n)
    build_tree(arr, 0, n-1, tree, 0)
    queries = int(stdin.readline())
    for q in range(queries):
        query = stdin.readline().split()
        q_type = query[0]
        if q_type == "U":
            update_tree(arr, tree, 0, n-1, int(query[1])-1, int(query[2]), 0)
        else:
            res = query_tree(arr, tree, 0, n-1, int(query[1])-1, int(query[2])-1, 0)[0]
            stdout.write(str(res)+"\n")
    


if __name__ == "__main__":
    main()
