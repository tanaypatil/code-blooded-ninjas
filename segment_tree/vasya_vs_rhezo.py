"""
Vasya vs Rhezo
Send Feedback
Queen Vasya is preparing for a war against Rhezo. She has N warriors in total arranged in a line. Let us number the warriors by numbers from 1 to N. She will fight Rhezo's army for Q days, and each day she can choose only one warrior.
For each warrior, we know 2 values associated with him, let us call these A and B. Each day Vasya can choose her warrior from a range Li to Ri, she must choose the warrior with maximum A value. If there is more than 1 warrior having the same maximum A value, she chooses the warrior with minimum B value. If still there is more than 1 warrior with same maximum A value and same minimum B value, she chooses the one with lower index in line.
You being the hand of Queen Vasya, need to help her in choosing the warrior for each day.
"""

def build_tree(arr, start, end, tree, treenode):
    if start == end:
        tree[treenode] = start
        return
    mid = (start + end) // 2
    build_tree(arr, start, mid, tree, 2 * treenode + 1)
    build_tree(arr, mid + 1, end, tree, 2 * treenode + 2)
    if arr[tree[2 * treenode + 1]][0] > arr[tree[2 * treenode + 2]][0]:
        tree[treenode] = tree[2 * treenode + 1]
    elif arr[tree[2 * treenode + 1]][0] < arr[tree[2 * treenode + 2]][0]:
        tree[treenode] = tree[2 * treenode + 2]
    else:
        if arr[tree[2 * treenode + 1]][1] < arr[tree[2 * treenode + 2]][1]:
            tree[treenode] = tree[2 * treenode + 1]
        elif arr[tree[2 * treenode + 1]][1] > arr[tree[2 * treenode + 2]][1]:
            tree[treenode] = tree[2 * treenode + 2]
        else:
            tree[treenode] = min(tree[2 * treenode + 1], tree[2 * treenode + 2])


def query_tree(arr, tree, start, end, s, e, treenode):
    if e < start or s > end:
        return -1

    if start >= s and end <= e:
        return tree[treenode]

    mid = (start + end) // 2
    opt1 = query_tree(arr, tree, start, mid, s, e, 2 * treenode + 1)
    opt2 = query_tree(arr, tree, mid + 1, end, s, e, 2 * treenode + 2)
    ret = 0
    if opt1 == -1 and opt2 != -1:
        return opt2
    if opt1 != -1 and opt2 == -1:
        return opt1
    if arr[opt1][0] > arr[opt2][0]:
        ret = opt1
    elif arr[opt1][0] < arr[opt2][0]:
        ret = opt2
    else:
        if arr[opt1][1] < arr[opt2][1]:
            ret = opt1
        elif arr[opt1][1] > arr[opt2][1]:
            ret = opt2
        else:
            ret = min(opt1, opt2)
    return ret
    


def main():
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    arr = [[a[i], b[i]] for i in range(n)]
    tree = [0] * (4 * n)
    build_tree(arr, 0, n - 1, tree, 0)
    queries = int(input())
    for q in range(queries):
        l, r = map(int, input().strip().split())
        print(query_tree(arr, tree, 0, n - 1, l - 1, r - 1, 0) + 1)


if __name__ == "__main__":
    main()
