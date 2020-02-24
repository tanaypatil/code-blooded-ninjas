
n = int(input())
matrix = []
s = 0
for i in range(n):
    matrix.append(list(map(int, input().split())))
for index1,i in enumerate(matrix):
    for index2,j in enumerate(i):
        if index1 == 0 or index1 == n-1:
            s += j
        elif index2 == 0 or index2 == n-1:
            s += j
        elif index1 == index2 or abs(index1+index2) == n-1:
            s += j
print(s)