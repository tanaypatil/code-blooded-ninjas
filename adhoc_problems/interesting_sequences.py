"""
Professor Jain has a class full of notorious students. To get anything done from them is a herculean task. Prof Jain wanted to organize a test. He gave this responsibility to Aahad. Aahad did an excellent job of organizing the test. As a reward, the professor gave him an sequence of numbers to play with. But Aahad likes playing with "interesting" sequence of numbers, which are sequences that have equal elements.
Now, the problem is - Prof Jain has a sequence with elements, and that sequence isn't always "interesting”. To ensure sequence has equal elements, Prof Jain has 2 options:
1) Choose two elements of sequence . DECREASE the first element by 1 and INCREASE the second element by 1. This operation costs 'k' coins.
2) Choose one element of array and INCREASE it by 1. This operation costs 'l' coins.
What’s the minimum number of coins Prof Jain needs to turn his sequence into a “interesting" sequence for Aahad?
"""
#Write your code here
def get_counts(arr, x):
    increasing = decreasing = 0
    for a in arr:
        if a > x:
            decreasing += a-x
        elif a < x:
            increasing += x-a
    return increasing, decreasing


def main():
    n, k, l = map(int, input().split())
    arr = list(map(int, input().split()))
    min_element = min(arr)
    max_element = max(arr)
    if min_element == max_element:
        cost = 0
    else:
        cost = 999999999
    for i in range(min_element, max_element+1):
        increasing, decreasing = get_counts(arr, i)
        if increasing >= decreasing:
            cost = min(cost, k*decreasing+l*(increasing-decreasing))
    print(cost)



if __name__ == "__main__":
    main()
