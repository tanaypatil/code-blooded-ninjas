"""
Fractional Knapsack
Send Feedback
You want to paint your house. The total area of your house is D units. There are a total of N workers. The ith worker is available after time Ti, has hiring cost Xi and speed Yi. This means he becomes available for hiring from time Ti and remains available after that. Once available, you can hire him with cost Xi, after which he will start painting the house immediately, covering exactly Yi units of house with paint per time unit. You may or may not hire a worker and can also hire or fire him at any later point of time. However, no more than 1 worker can be painting the house at a given time.
Since you want the work to be done as fast as possible, figure out a way to hire the workers, such that your house gets painted at the earliest possible time, with minimum cost to spend for hiring workers.
Note: You can hire a previously hired worker without paying him again.
"""
## Read input as specified in the question.
## Print output as specified in the question.
def main():
    n, d = map(int, input().split())
    w = []
    for i in range(n):
        t, x, y = map(int, input().strip().split())
        w.append((t, x, y))
    w = sorted(w, key=lambda x: (x[0], x[2], x[1]))
    maxarea = w[0][2]
    total_painted = 0
    total_cost = 0
    lasttime = w[0][0]
    for i in w[1:n]:
        painted = maxarea * (i[0]-lasttime)
        total_painted += painted
        if total_painted >= d:
            break
        if i[2] > maxarea:
            maxarea = i[2]
            total_cost += i[1]
        lasttime = i[0]
    print(total_cost)
    


if __name__ == "__main__":
    main()
