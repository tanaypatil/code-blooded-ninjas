"""
Maximum Sum Rectangle
Send Feedback
Given a 2D array, find the maximum sum rectangle in it. In other words find maximum sum over all rectangles in the matrix.
"""
def main():
    r, c = map(int, input().strip().split())
    arr = [list(map(int, input().strip().split())) for _ in range(r)]
    temp_arr = []
    global_max = -999999999
    for start in range(c-1):
        for end in range(start,c):
            if start == end:
                temp_arr = [arr[i][start] for i in range(r)]
            else:
                temp_arr = [temp_arr[i]+arr[i][end] for i in range(r)]
            temp_sum = 0
            max_temp_sum = 0
            for t in temp_arr:
                temp_sum += t
                if temp_sum > max_temp_sum:
                    max_temp_sum = temp_sum
                if temp_sum < 0:
                    temp_sum = 0
            if max_temp_sum == 0:
                max_temp_sum = max(temp_arr)
            global_max = max(global_max, max_temp_sum)
    print(global_max)


if __name__ == "__main__":
    main()