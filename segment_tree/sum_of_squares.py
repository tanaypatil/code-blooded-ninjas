"""
Sum Of Squares
Send Feedback
Segment trees are extremely useful. In particular "Lazy Propagation" (i.e. see here, for example) allows one to compute sums over a range in O(lg(n)), and update ranges in O(lg(n)) as well. In this problem you will compute something much harder:
The sum of squares over a range with range updates of 2 types:
1) increment in a range
2) set all numbers the same in a range.
"""


def build_tree(arr, start, end, tree, treenode):
    if start == end:
        tree[treenode] = [arr[start]**2, arr[start]]
        return
    mid = (start + end) // 2
    build_tree(arr, start, mid, tree, 2*treenode+1)
    build_tree(arr, mid+1, end, tree, 2*treenode+2)
    tree[treenode] = [tree[2*treenode+1][0]+tree[2*treenode+2][0], tree[2*treenode+1][1]+tree[2*treenode+2][1]]


def increment_child(arr, tree, lazy_tree, start, end, treenode, value):
    if start > end:
        return

    if lazy_tree[treenode][0] != 0:
        if lazy_tree[treenode][1] == "i":
            lazy_tree[treenode] = [value+lazy_tree[treenode][0], "i"]
        else:
            ss = (end-start+1)*lazy_tree[treenode][0]**2
            su = (end-start+1)*lazy_tree[treenode][0]
            tree[treenode][0] = ss
            tree[treenode][1] = su
            if start != end:
                lazy_tree[2*treenode+1] = [lazy_tree[treenode][0], "c"]
                lazy_tree[2*treenode+2] = [lazy_tree[treenode][0], "c"]
            lazy_tree[treenode] = [value, "i"]
    


def increment_tree(arr, tree, lazy_tree, start, end, s, e, value, treenode):
    if start > end:
        return
    mid = (start + end) // 2
    if lazy_tree[treenode][0] != 0:
        if lazy_tree[treenode][1] == "i":
            ss = (end-start+1)*lazy_tree[treenode][0]**2 + 2*value*tree[treenode][1]
            su = (end-start+1)*lazy_tree[treenode][0]
            tree[treenode][0] += ss
            tree[treenode][1] += su
            if start != end:
                increment_child(arr, tree, lazy_tree, start, mid, 2*treenode+1, lazy_tree[treenode][0])
                increment_child(arr, tree, lazy_tree, mid+1, end, 2*treenode+2, lazy_tree[treenode][0])
        else:
            ss = (end-start+1)*lazy_tree[treenode][0]**2
            su = (end-start+1)*lazy_tree[treenode][0]
            tree[treenode][0] = ss
            tree[treenode][1] = su
            if start != end:
                lazy_tree[2*treenode+1] = [lazy_tree[treenode][0], "c"]
                lazy_tree[2*treenode+2] = [lazy_tree[treenode][0], "c"]
        lazy_tree[treenode] = [0, ""]
    if e < start or s > end:
        return

    if start >= s and e >= end:
        ss = (end-start+1)*value**2 + 2*value*tree[treenode][1]
        su = (end-start+1)*value
        tree[treenode][0] += ss
        tree[treenode][1] += su
        if start != end:
            increment_child(arr, tree, lazy_tree, start, mid, 2*treenode+1, value)
            increment_child(arr, tree, lazy_tree, mid+1, end, 2*treenode+2, value)
        return
    
    increment_tree(arr, tree, lazy_tree, start, mid, s, e, value, 2*treenode+1)
    increment_tree(arr, tree, lazy_tree, mid+1, end, s, e, value, 2*treenode+2)
    tree[treenode][0] = tree[2*treenode+1][0] + tree[2*treenode+2][0]
    tree[treenode][1] = tree[2*treenode+1][1] + tree[2*treenode+2][1]



def change_tree(arr, tree, lazy_tree, start, end, s, e, value, treenode):
    if start > end:
        return
    
    if e < start or s > end:
        return

    if start >= s and e >= end:
        ss = (end-start+1)*value**2
        su = (end-start+1)*value
        tree[treenode][0] = ss
        tree[treenode][1] = su
        if start != end:
            lazy_tree[2*treenode+1] = [value, "c"]
            lazy_tree[2*treenode+2] = [value, "c"]
        return

    mid = (start + end) // 2
    change_tree(arr, tree, lazy_tree, start, mid, s, e, value, 2*treenode+1)
    change_tree(arr, tree, lazy_tree, mid+1, end, s, e, value, 2*treenode+2)
    tree[treenode][0] = tree[2*treenode+1][0] + tree[2*treenode+2][0]
    tree[treenode][1] = tree[2*treenode+1][1] + tree[2*treenode+2][1]



def query_tree(arr, tree, lazy_tree, start, end, s, e, treenode):

    if lazy_tree[treenode][0] != 0:
        if lazy_tree[treenode][1] == "i":
            ss = (end-start+1)*lazy_tree[treenode][0]**2 + 2*value*tree[treenode][1]
            su = (end-start+1)*lazy_tree[treenode][0]
            tree[treenode][0] += ss
            tree[treenode][1] += su
            if start != end:
                mid = (start + end) // 2
                increment_child(arr, tree, lazy_tree, start, mid, 2*treenode+1, lazy_tree[treenode][0])
                increment_child(arr, tree, lazy_tree, mid+1, end, 2*treenode+2, lazy_tree[treenode][0])
        else:
            ss = (end-start+1)*lazy_tree[treenode][0]**2
            su = (end-start+1)*lazy_tree[treenode][0]
            tree[treenode][0] = ss
            tree[treenode][1] = su
            if start != end:
                lazy_tree[2*treenode+1] = [lazy_tree[treenode][0], "c"]
                lazy_tree[2*treenode+2] = [lazy_tree[treenode][0], "c"]
        lazy_tree[treenode] = [0, ""]

    if e < start or s > end:
        return [0, 0]

    if start >= s and end <= e:
        return tree[treenode]

    mid = (start + end) // 2
    opt1 = query_tree(arr, tree, lazy_tree, start, mid, s, e, 2*treenode+1)
    opt2 = query_tree(arr, tree, lazy_tree, mid+1, end, s, e, 2*treenode+2)
    return [opt1[0]+opt2[0], opt1[1]+opt2[1]]


def main():
    tc = int(input())
    for t in range(tc):
        n, queries = map(int, input().strip().split())
        arr = list(map(int, input().strip().split()))
        tree = [[0, 0] for _ in range(4*n)]
        lazy_tree = [[0, ""] for _ in range(4*n)]
        build_tree(arr, 0, n-1, tree, 0)
        print("Case " + str(t+1) + ":")
        for q in range(queries):
            query = list(map(int, input().strip().split()))
            if len(query) == 4:
                q_type, i, j, x = query[0], query[1], query[2], query[3]
            else:
                q_type, i, j = query[0], query[1], query[2]
            if q_type == 2:
                print(query_tree(arr, tree, lazy_tree, 0, n-1, i-1, j-1, 0)[0])
            elif q_type == 1:
                increment_tree(arr, tree, lazy_tree, 0, n-1, i-1, j-1, x, 0)
            else:
                change_tree(arr, tree, lazy_tree, 0, n-1, i-1, j-1, x, 0)



if __name__ == "__main__":
    main()
