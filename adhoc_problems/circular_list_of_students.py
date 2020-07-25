"""
You are given a circular list of students as follows:
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11
This list is circular, means that 11 will follow 0 again. You will be given the student number ‘i’ and some position ‘p’. You will have to tell that if the list will start from (i+1)th student, then which student will be at pth position.
"""
def main():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    tc = int(input())
    for t in range(tc):
        i, p = map(int, input().split())
        print(arr[(i+p)%12])


if __name__ == "__main__":
    main()
