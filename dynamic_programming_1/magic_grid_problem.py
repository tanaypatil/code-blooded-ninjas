"""
Magic Grid Problem
Send Feedback
You are given a magrid S ( a magic grid ) having R rows and C columns. Each cell in this magrid has either a Hungarian horntail dragon that our intrepid hero has to defeat, or a flask of magic potion that his teacher Snape has left for him. A dragon at a cell (i,j) takes away |S[i][j]| strength points from him, and a potion at a cell (i,j) increases Harry's strength by S[i][j]. If his strength drops to 0 or less at any point during his journey, Harry dies, and no magical stone can revive him.
Harry starts from the top-left corner cell (1,1) and the Sorcerer's Stone is in the bottom-right corner cell (R,C). From a cell (i,j), Harry can only move either one cell down or right i.e., to cell (i+1,j) or cell (i,j+1) and he can not move outside the magrid. Harry has used magic before starting his journey to determine which cell contains what, but lacks the basic simple mathematical skill to determine what minimum strength he needs to start with to collect the Sorcerer's Stone. Please help him once again.
"""
def print_arr(a):
    for i in range(len(a)):
        print(a[i])
    print("-----")

def main():
    tc = int(input())
    for t in range(tc):
        r, c = map(int, input().strip().split())
        arr = [list(map(int, input().strip().split())) for _ in range(r)]
        dp_arr = [[0]*c for _ in range(r)]
        dp_arr[r-1][c-1] = 0
        dp_arr[r-1][c-2] = dp_arr[r-1][c-1]- arr[r-1][c-2] + 1
        dp_arr[r-2][c-1] = dp_arr[r-1][c-1]- arr[r-2][c-1] + 1
        i = c-3
        while i >= 0:
            if arr[r-1][i] < 0:
                dp_arr[r-1][i] = dp_arr[r-1][i] = dp_arr[r-1][i+1] - arr[r-1][i] if dp_arr[r-1][i+1] - arr[r-1][i] + 1 > 0 else 1
            else:
                dp_arr[r-1][i] = dp_arr[r-1][i+1] - arr[r-1][i] if dp_arr[r-1][i+1] - arr[r-1][i] > 0 else 1
            i -= 1
        # print_arr(dp_arr)
        i = r-3
        while i >= 0:
            if arr[i][c-1] < 0:
                dp_arr[i][c-1] = dp_arr[i+1][c-1] - arr[i][c-1] if dp_arr[i+1][c-1] - arr[i][c-1] + 1 > 0 else 1
            else:
                dp_arr[i][c-1] = dp_arr[i+1][c-1] - arr[i][c-1] if dp_arr[i+1][c-1] - arr[i][c-1] > 0 else 1
            i -= 1
        # print_arr(dp_arr)
        for i in range(r-2, -1, -1):
            for j in range(c-2, -1, -1):
                to_add = min(dp_arr[i+1][j], dp_arr[i][j+1])
                if arr[i][j] < 0:
                    dp_arr[i][j] = dp_arr[i][j] = to_add - arr[i][j] if to_add - arr[i][j] + 1 > 0 else 1
                else:
                    dp_arr[i][j] = to_add - arr[i][j] if to_add - arr[i][j] > 0 else 1
        # print_arr(dp_arr)
        print(dp_arr[0][0])
            
                

if __name__ == "__main__":
    main()
