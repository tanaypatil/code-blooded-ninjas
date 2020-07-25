"""
Minimum In SubArray
Send Feedback
Range Minimum Query
Given an array A of size N, there are two types of queries on this array.
1) q l r: In this query you need to print the minimum in the sub-array A[l:r].
2) u x y: In this query you need to update A[x]=y.
"""
def build_tree(arr, start, end, tree, treenode):
    if start == end:
        tree[treenode] = arr[start]
        return
    mid = (start + end) // 2
    build_tree(arr, start, mid, tree, 2*treenode+1)
    build_tree(arr, mid+1, end, tree, 2*treenode+2)
    tree[treenode] = min(tree[2*treenode+2], tree[2*treenode+1])


def update_tree(arr, tree, start, end, index, value, treenode):
    if start == end:
        arr[index] = value
        tree[treenode] = value
        return
    mid = (start + end) // 2
    if start <= index <= mid:
        update_tree(arr, tree, start, mid, index, value, 2*treenode+1)
    else:
        update_tree(arr, tree, mid+1, end, index, value, 2*treenode+2)
    tree[treenode] = min(tree[2*treenode+1], tree[2*treenode+2])


def query_tree(arr, tree, start, end, s, e, treenode):
    if e < start or s > end:
        return 99999

    if start >= s and end <= e:
        return tree[treenode]

    mid = (start + end) // 2
    opt1 = query_tree(arr, tree, start, mid, s, e, 2*treenode+1)
    opt2 = query_tree(arr, tree, mid+1, end, s, e, 2*treenode+2)
    return min(opt1, opt2)
    


def main():
    n, queries = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    tree = [999999]*(4*n)
    build_tree(arr, 0, n-1, tree, 0)
    for q in range(queries):
        query = input().split()
        q_type = query[0]
        if q_type == "u":
            update_tree(arr, tree, 0, n-1, int(query[1])-1, int(query[2]), 0)
        else:
            print(query_tree(arr, tree, 0, n-1, int(query[1])-1, int(query[2])-1, 0))
    


if __name__ == "__main__":
    main()
