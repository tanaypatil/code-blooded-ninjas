"""
Weighted Job Scheduling
Send Feedback
You are given N jobs where every job is represented as:
1.Start Time
2.Finish Time
3.Profit Associated
Find the maximum profit subset of jobs such that no two jobs in the subset overlap.
"""
## Read input as specified in the question.
## Print output as specified in the question.

def bin_search(jobs, start_time, index):
    start = 0
    end = index
    mid = (start+end)//2
    f = 0
    ret = 0
    d = set()
    while start <= mid:
        if jobs[mid] in d:
            break
        d.add(jobs[mid])
        if jobs[mid][1] <= start_time:
            f = 1
            ret = mid
            start = mid
        else:
            end = mid
        mid = (start+end)//2
    if f == 0:
        return -1
    else:
        return ret


def main():
    n = int(input())
    jobs = []
    for i in range(n):
        start, end, profit = map(int, input().strip().split())
        jobs.append((start, end, profit))
    jobs = sorted(jobs, key=lambda x: x[1])
    profit = jobs[0][2]
    profit_arr = [profit]
    for index, job in enumerate(jobs[1:], 1):
        if job[0] >= jobs[index-1][1]:
            profit_arr.append(profit_arr[-1] + job[2])
        else:
            i = bin_search(jobs, job[0], index)
            if i != -1:
                profit_arr.append(max(profit_arr[-1], profit_arr[i] + job[2]))
            else:
                profit_arr.append(max(profit_arr[-1], job[2]))
    print(max(profit_arr))
                
                
if __name__ == "__main__":
    main()
