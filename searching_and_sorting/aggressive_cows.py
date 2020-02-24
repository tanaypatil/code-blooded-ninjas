def canArrangeCows(stops, cows, d):
    placed_cows = 0
    for index,stop in enumerate(stops):
        if index == 0:
            placed_cows += 1
            last_stop = 0
        if stops[index] - stops[last_stop] >= d:
            placed_cows += 1
            last_stop = index
        if placed_cows == cows:
            break
    return (placed_cows == cows)
        


def main():
    tc = int(input())
    for t in range(tc):
        n, c = map(int, input().strip().split())
        stops = []
        for i in range(n):
            stops.append(int(input()))
        stops.sort()
        min_d = 0
        max_d = max(stops) - min(stops)
        mid_d = (min_d+max_d)//2 if (min_d + max_d) % 2 == 0 else ((min_d+max_d)//2)+1
        
        while True:
            if mid_d == min_d:
                break
            else:
                if canArrangeCows(stops, c, mid_d):
                    min_d = mid_d
                else:
                    max_d = mid_d - 1
                mid_d = (min_d+max_d)//2 if (min_d + max_d) % 2 == 0 else ((min_d+max_d)//2)+1
        
        print(mid_d)
        
        



if __name__ == "__main__":
    main()
