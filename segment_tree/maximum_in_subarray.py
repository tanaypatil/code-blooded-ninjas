"""
Maximum Sum In Subarray
Send Feedback
You are given a sequence A[1], A[2], ..., A[N] . ( |A[i]| ≤ 15007 , 1 ≤ N ≤ 50000 ). A query is defined as follows:
Query(x,y) = Max { a[i]+a[i+1]+...+a[j] ; x ≤ i ≤ j ≤ y }.
Given M queries, your program must output the results of these queries.
"""
from sys import stdin, stdout


def build_tree(arr, start, end, tree, treenode):
    if start == end:
        tree[treenode] = [arr[start], arr[start], arr[start], arr[start]]
        return
    mid = (start + end) // 2
    build_tree(arr, start, mid, tree, 2*treenode+1)
    build_tree(arr, mid+1, end, tree, 2*treenode+2)
    tree[treenode] = [0]*4
    tree[treenode][0] = tree[2*treenode+1][0] + tree[2*treenode+2][0]
    best_prefix_sum = max(tree[2*treenode+1][1], tree[2*treenode+1][0] + tree[2*treenode+2][1])
    best_suffix_sum = max(tree[2*treenode+2][2], tree[2*treenode+2][0] + tree[2*treenode+1][2])
    tree[treenode][1] = best_prefix_sum
    tree[treenode][2] = best_suffix_sum
    max_sum = max(tree[2*treenode+1][3], tree[2*treenode+2][3], tree[2*treenode+1][0] + tree[2*treenode+2][1], 
                 tree[2*treenode+2][0] + tree[2*treenode+1][2], tree[2*treenode+1][2] + tree[2*treenode+2][1])
    tree[treenode][3] = max_sum
    


def update_tree(arr, tree, start, end, index, value, treenode):
    if start == end:
        arr[index] = value
        tree[treenode] = [value, value, value, value]
        return
    mid = (start + end) // 2
    if start <= index <= mid:
        update_tree(arr, tree, start, mid, index, value, 2*treenode+1)
    else:
        update_tree(arr, tree, mid+1, end, index, value, 2*treenode+2)
    tree[treenode] = [0]*4
    tree[treenode][0] = tree[2*treenode+1][0] + tree[2*treenode+2][0]
    best_prefix_sum = max(tree[2*treenode+1][1], tree[2*treenode+1][0] + tree[2*treenode+2][1])
    best_suffix_sum = max(tree[2*treenode+2][2], tree[2*treenode+2][0] + tree[2*treenode+1][2])
    tree[treenode][1] = best_prefix_sum
    tree[treenode][2] = best_suffix_sum
    max_sum = max(tree[2*treenode+1][3], tree[2*treenode+2][3], tree[2*treenode+1][0] + tree[2*treenode+2][1], 
                 tree[2*treenode+2][0] + tree[2*treenode+1][2], tree[2*treenode+1][2] + tree[2*treenode+2][1])
    tree[treenode][3] = max_sum


def query_tree(arr, tree, start, end, s, e, treenode):
    if e < start or s > end:
        return [-9999999, -9999999, -9999999, -9999999]

    if start >= s and end <= e:
        return tree[treenode]

    mid = (start + end) // 2
    opt1 = query_tree(arr, tree, start, mid, s, e, 2*treenode+1)
    opt2 = query_tree(arr, tree, mid+1, end, s, e, 2*treenode+2)
    node = [0]*4
    node[0] = opt1[0] + opt2[0]
    best_prefix_sum = max(opt1[1], opt1[0] + opt2[1])
    best_suffix_sum = max(opt2[2], opt2[0] + opt1[2])
    node[1] = best_prefix_sum
    node[2] = best_suffix_sum
    max_sum = max(opt1[3], opt2[3], opt1[2] + opt2[1])
    node[3] = max_sum
    return node


def main():
    n = input().strip()
    while n == '':
        n = input().strip()
    n = int(n)
    arr = list(map(int, input().strip().split()))
    if len(arr) != n:
        arr += list(map(int, input().strip().split()))[n-len(arr)]
    queries = int(input())
    tree = [0]*(4*n)
    build_tree(arr, 0, n-1, tree, 0)
    for q in range(queries):
        x, y = map(int, input().split())
        print(query_tree(arr, tree, 0, n-1, x-1, y-1, 0)[3])
    


if __name__ == "__main__":
    main()
