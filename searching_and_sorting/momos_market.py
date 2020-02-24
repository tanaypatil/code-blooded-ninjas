

def main():
    n = int(input())
    prices = list(map(int, input().strip().split()))
    q = int(input())
    amount = []
    for i in range(q):
        a = int(input().strip())
        amount.append(a)
    for i in range(q):
        money_spent = 0
        index = 0
        for index,price in enumerate(prices):
            if money_spent + price > amount[i]:
                break
            money_spent += price
        print(index, amount[i]-money_spent)
    


if __name__ == "__main__":
    main()