"""
Find The Cube Free Number
Send Feedback
A cube free number is a number who’s none of the divisor is a cube number (A cube number is a cube of a integer like 8 (2 * 2 * 2) , 27 (3 * 3 * 3) ). So cube free numbers are 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 17, 18 etc (we will consider 1 as cube free). 8, 16, 24, 27, 32 etc are not cube free number. So the position of 1 among the cube free numbers is 1, position of 2 is 2, 3 is 3 and position of 10 is 9. Given a positive number you have to say if its a cube free number and if yes then tell its position among cube free numbers.
"""
from collections import defaultdict
from sys import stdin, stdout



def main():
    
    is_not_cube_free = defaultdict(bool)
    
    for i in range(2, 101):
        if not is_not_cube_free[i]:
            cube = i**3
            j = 1
            while cube*j <= 10**6:
                is_not_cube_free[cube*j] = True
                j += 1
    
    indexes = defaultdict(int)
    indexes[1] = 1
    index = 1
    for i in range(2, 10**6):
        if not is_not_cube_free[i]:
            index += 1
            indexes[i] = index

    tc = int(stdin.readline())
    for t in range(tc):
        n = int(stdin.readline())
        if indexes[n] == 0:
            stdout.write("Case "+str(t+1)+": Not Cube Free\n")
        else:
            stdout.write("Case "+str(t+1)+": "+str(indexes[n])+"\n")
        



if __name__ == "__main__":
    main()
