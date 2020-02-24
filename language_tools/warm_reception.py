
def main():
    n = int(input())
    arrivals = list(map(int, input().split()))
    departures = list(map(int, input().split()))
    all_times = arrivals + departures
    max_chairs = 0
    for time in all_times:
        current_sum = 0
        for a in arrivals:
            if a <= time:
                current_sum += 1
        for d in departures:
            if d < time:
                current_sum -= 1
        max_chairs = max(max_chairs, current_sum)
    print(max_chairs)
    
        
        
                    

if __name__ == "__main__":
    main()