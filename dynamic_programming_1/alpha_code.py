"""
AlphaCode-Question
Send Feedback
Alice and Bob need to send secret messages to each other and are discussing ways to encode their messages:
Alice: “Let’s just use a very simple code: We’ll assign ‘A’ the code word 1, ‘B’ will be 2, and so on down to ‘Z’ being assigned 26.”

Bob: “That’s a stupid code, Alice. Suppose I send you the word ‘BEAN’ encoded as 25114. You could decode that in many different ways!”

Alice: “Sure you could, but what words would you get? Other than ‘BEAN’, you’d get ‘BEAAD’, ‘YAAD’, ‘YAN’, ‘YKD’ and ‘BEKD’. I think you would be able to figure out the correct decoding. And why would you send me the word ‘BEAN’ anyway?”

Bob: “OK, maybe that’s a bad example, but I bet you that if you got a string of length 5000 there would be tons of different decodings and with that many you would find at least two different ones that would make sense.”

Alice: “How many different decodings?”

Bob: “Jillions!”
For some reason, Alice is still unconvinced by Bob’s argument, so she requires a program that will determine how many decodings there can be for a given string using her code.
"""
prime = 1000000007


def encode_count(arr, count_dict):
    if len(arr) == 0 or len(arr) == 1:
        return 1
    if len(arr) in count_dict:
        return count_dict[len(arr)]
    count = encode_count(arr[:-1], count_dict)%prime if arr[-1] != 0 else 0
    count = (count + encode_count(arr[:-2], count_dict)%prime)%prime if 10 <= arr[-2]*10 + arr[-1]  <= 26 else count
    count_dict[len(arr)] = count
    return count


def encode_count_iterative(arr):
    count_arr = [1, 1] if arr[1] != 0 else [1, 0]
    for i in range(2, len(arr)+1):
        count = count_arr[i-1] if arr[i-1] != 0 else 0
        if 10 <= arr[i-2]*10 + arr[i-1] <= 26:
            count += count_arr[i-2]%prime
        count_arr.append(count%prime)
    return(count_arr[-1])



def main():
    while True:
        arr = input().strip()
        arr = list(arr)
        arr = list(map(int, arr))
        if arr[0] == 0:
            break
        if len(arr) == 1:
            print(1)
        else:
            print(encode_count_iterative(arr))



if __name__ == "__main__":
    main()
