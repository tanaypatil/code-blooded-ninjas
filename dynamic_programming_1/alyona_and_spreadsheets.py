"""
Alyona and Spreadsheet
Send Feedback
During the lesson small girl Alyona works with one famous spreadsheet computer program and learns how to edit tables.
Now she has a table filled with integers. The table consists of n rows and m columns. By ai, j we will denote the integer located at the i-th row and the j-th column. We say that the table is sorted in non-decreasing order in the column j if ai, j ≤ ai + 1, j for all i from 1 to n - 1.
Teacher gave Alyona k tasks. For each of the tasks two integers l and r are given and Alyona has to answer the following question: if one keeps the rows from l to r inclusive and deletes all others, will the table be sorted in non-decreasing order in at least one column? Formally, does there exist such j that ai, j ≤ ai + 1, j for all i from l to r - 1 inclusive.
Alyona is too small to deal with this task and asks you to help!
"""
from sys import stdin, stdout


memo = {}


def is_sorted(l, r, arr):
    if l == r or r < 0:
        return range(len(arr[0]))
    else:
        if (l, r) in memo:
            return memo[(l, r)]
        sub = is_sorted(l+1, r, arr)
        if len(sub) == 0:
            memo[(l, r)] = []
            return []
        f = []
        for s in sub:
            if arr[l][s] <= arr[l+1][s]:
                f.append(s)
        if len(f) > 0:
            memo[(l, r)] = f
            return f
        else:
            memo[(l, r)] = []
            return []


def main():
    n, m = map(int, stdin.readline().strip().split())
    arr = [list(map(int, stdin.readline().strip().split())) for _ in range(n)]
    tc = int(stdin.readline())
    for t in range(tc):
        l, r = map(int, stdin.readline().strip().split())
        if len(is_sorted(l-1, r-1, arr)) > 0:
            stdout.write("Yes\n")
        else:
            stdout.write("No\n")



if __name__ == "__main__":
    main()
