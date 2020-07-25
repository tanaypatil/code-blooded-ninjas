"""
Jon Snow and his favourite number
Send Feedback
Jon Snow now has to fight with White Walkers. He has n rangers, each of which has his own strength. Also Jon Snow has his favourite number x. Each ranger can fight with a white walker only if the strength of the white walker equals his strength. He however thinks that his rangers are weak and need to improve. Jon now thinks that if he takes the bitwise XOR of strengths of some of rangers with his favourite number x, he might get soldiers of high strength. So, he decided to do the following operation k times:
Arrange all the rangers in a straight line in the order of increasing strengths.
Take the bitwise XOR of the strength of each alternate ranger with x and update it's strength.
Suppose, Jon has 5 rangers with strengths [9, 7, 11, 15, 5] and he performs the operation 1 time with x = 2. He first arranges them in the order of their strengths, [5, 7, 9, 11, 15]. Then he does the following:
The strength of first ranger is updated to 5 xor 2, i.e. 7.
The strength of second ranger remains the same, i.e. 7.
The strength of third ranger is updated to 9 xor 2, i.e. 11.
The strength of fourth ranger remains the same, i.e. 11.
The strength of fifth ranger is updated to 15 xor 2, i.e. 13.
The new strengths of the 5 rangers are [7, 7, 11, 11, 13]
Now, Jon wants to know the maximum and minimum strength of the rangers after performing the above operations k times. He wants your help for this task. Can you help him?
"""
from collections import Counter, defaultdict, OrderedDict
from sys import stdin, stdout


def main():
    n, k, x = map(int, stdin.readline().strip().split())
    arr = list(map(int, stdin.readline().strip().split()))
    new_arr = arr.copy()
    count_dict = {}
    count_dict = Counter(new_arr)
    for i in range(k):
        count_dict = OrderedDict(sorted(count_dict.items()))
        count = 0
        new_dict = defaultdict(int)
        for k, v in count_dict.items():
            to_be_taken = 0
            if count % 2 == 0 and v % 2 != 0:
                to_be_taken = (v+1)//2
            else:
                to_be_taken = v//2
            new_dict[k] += v - to_be_taken
            new_dict[k^x] += to_be_taken
            count += v
        count_dict = new_dict
    final_dict = defaultdict(int)
    for k, v in count_dict.items():
        if v != 0:
            final_dict[k] = v
    res = str(max(final_dict.keys()))+" "+str(min(final_dict.keys()))
    stdout.write(res+"\n")
            


if __name__ == "__main__":
    main()
