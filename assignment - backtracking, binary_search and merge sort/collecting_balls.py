"""
There are ‘n’ number of balls in a container. Mr. Sharma and Singh want to take balls out from the container. At each step, Mr. Sharma took ‘k’ balls out of the box and Mr. Singh took one-tenth of the remaining balls. Suppose there are 29 balls at the moment and k=4. Then, Mr. Sharma will take 4 balls and Mr. Singh will take 2 balls (29-4 = 25; 25/10 = 2). If there are less than ‘k’ balls remaining at some moment, then Mr. Sharma will take all the balls which will get the container empty. The process will last until the container becomes empty. Your task is to choose minimal ‘k’ for Mr. Sharma such that Mr. Sharma will take at least half of the balls from the container.
"""
def canCollect(total, k):
    sharma = 0
    singh = 0
    n = total
    if n % 2 == 0:
        c = (total//2)
    else:
        c = (total//2)+1
    while n >= k:
        n -= k
        sharma += k
        if n == 0 and sharma >= c:
            return True
        singh += (n//10)
        n -= n//10
    if sharma + n >= c:
        return True
    return False
            
        
def main():
    n = int(input())
    min_limit = 1
    max_limit = n//2
    mid = (min_limit+max_limit)//2
    if n//10 == 0:
        print(1)
        return
    while min_limit != mid:
        if canCollect(n, mid):
            max_limit = mid
        else:
            min_limit = mid+1
        mid = (min_limit+max_limit)//2
    '''mid = 1
    while not canCollect(n, mid):
        mid += 1'''
    if canCollect(n, mid):
        print(mid)
    else:
        print(max_limit)
        


if __name__ == "__main__":
    main()
