"""
Our college team is going to the sports fest to play a football match with our coach. There are n players in our team, numbered from 1 to n.
The coach will know the position of another team hence create a winning strategy. He creates the position of every player in a specific order so that we will win and then he starts swapping two players at a time to form the positions.
He swaps payers in such a way that it can't be understood by another team:
1. Any player can swap with the player directly at front him
2. One player can swap at most with two other players
If the specific order is formed then our team will win otherwise we will lose
"""
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    f = 0
    swaps = 0
    for index, a in enumerate(arr):
        if abs(index-a+1) > 2:   
            f = 1
            break
        else:
            swaps += abs(index-a+1)
    if f == 1:
        print("NO")
    else:
        print("YES")
        print(swaps//2)
            

if __name__ == "__main__":
    main()