"""
Charlie and Pilots
Send Feedback
Charlie acquired airline transport company and to stay in business he needs to lower the expenses by any means possible. There are N pilots working for his company (N is even) and N/2 plane crews needs to be made. A plane crew consists of two pilots - a captain and his assistant. A captain must be older than his assistant. Each pilot has a contract granting him two possible salaries - one as a captain and the other as an assistant. A captain's salary is larger than assistant's for the same pilot. However, it is possible that an assistant has larger salary than his captain. Write a program that will compute the minimal amount of money Charlie needs to give for the pilots' salaries if he decides to spend some time to make the optimal (i.e. the cheapest) arrangement of pilots in crews.
"""
import sys


memo = {}


def count_min(assistants, n, x, captains):
    if n == 0:
        return 0
    if (n, x) in memo:
        return memo[(n, x)]
    if x == 0:
        ret = assistants[0] + count_min(assistants[1:], n-1, 1, captains[1:])
    elif x == n:
        ret = captains[0] + count_min(assistants[1:], n-1, x-1, captains[1:])
    else:
        opt1 = assistants[0] + count_min(assistants[1:], n-1, x+1, captains[1:])
        opt2 = captains[0] + count_min(assistants[1:], n-1, x-1, captains[1:])
        ret = min(opt1, opt2)
    memo[(n, x)] = ret
    return ret




def main():
    n = int(sys.stdin.readline())
    captains = []
    assistants = []
    for i in range(n):
        cap, ast = map(int, sys.stdin.readline().strip().split())
        captains.append(cap)
        assistants.append(ast)
    sys.stdout.write(str(count_min(assistants, n, 0, captains))+"\n")
            
        
    


if __name__ == "__main__":
    sys.setrecursionlimit(50000)
    main()

