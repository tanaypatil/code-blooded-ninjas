"""
A bulb can be ‘ON’ or ‘OFF’. Mr. Navdeep got ‘n’ number of bulbs and their status, whether they are ‘ON’ or ‘OFF’. Their status is represented in a string of size ‘n’ consisting of 0’s and 1’s, where ‘0’ represents the bulb is in ‘OFF’ condition and ‘1’ represent the bulb is ‘ON’. Mr. Navdeep has been given the task to light up all the bulbs.
He can perform two operations.
First, chose any segment of bulbs and reverse them means chose any substring and reverse it. E.g. “0 110 001” -> “0 011 001”. Substring (1, 3) is reversed here. This operation will cost him Rs. ‘X’.
Second, chose any segment of bulbs and reverse their present condition. i.e. if the bulb is ‘ON’, make it ‘OFF’ and if it is ‘OFF’, make it ‘ON’. E.g. “0 011 001” -> “0 100 001”. Substring (1, 3) is complemented. This operation will cost him Rs. ‘Y’.
You need to help Mr. Navdeep that how much minimum amount it will require to make all the bulbs lightened. (or make all the characters as ‘1’ in the representation string)
"""
def main():
    n, x, y = map(int, input().split())
    s = input()
    cost = 0
    i = 0
    if n == 1:
        if s[0] == "0":
            print(y)
        else:
            print(0)
    else:
        if y <= x:
            while i < n - 1:
                if s[i] == "0" and s[i+1] == "1":
                    cost += y
                i += 1
            cost = cost+y if s[-1] == "0" else cost
            print(cost)
        else:
            if "0" not in s:
                print(0)
            else:
                zero_count = 1 if s[-1] == "0" else 0
                while i < n-1:
                    if s[i] == "1" and s[i+1] == "0" and i != 0:
                        cost += x
                    if s[i] == "0":
                        zero_count += 1
                    i += 1
                cost = y if zero_count == 1 else cost+y
                print(cost)


if __name__ == "__main__":
    main()
