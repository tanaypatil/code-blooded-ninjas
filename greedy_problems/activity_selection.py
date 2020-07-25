"""
Activity Selection
Send Feedback
You are given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.
"""
## Read input as specified in the question.
## Print output as specified in the question.
def main():
    n = int(input())
    times = []
    for i in range(n):
        a, b = map(int, input().strip().split())
        times.append((a, b))
    sorted_times = sorted(times, key=lambda x: x[1])
    count = 1
    last_end = sorted_times[0][1]
    for i in range(1, n):
        if sorted_times[i][0] >= last_end:
            count += 1
            last_end = sorted_times[i][1]
    print(count)
    

if __name__ == "__main__":
    main()
