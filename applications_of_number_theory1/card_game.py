"""
Card Game
Send Feedback
Vova again tries to play some computer card game.
The rules of deck creation in this game are simple. Vova is given an existing deck of n cards and a magic number k. The order of the cards in the deck is fixed. Each card has a number written on it; number ai is written on the i-th card in the deck.
After receiving the deck and the magic number, Vova removes x (possibly x = 0) cards from the top of the deck, y (possibly y = 0) cards from the bottom of the deck, and the rest of the deck is his new deck (Vova has to leave at least one card in the deck after removing cards). So Vova's new deck actually contains cards x + 1, x + 2, ... n - y - 1, n - y from the original deck.
Vova's new deck is considered valid iff the product of all numbers written on the cards in his new deck is divisible by k. So Vova received a deck (possibly not a valid one) and a number k, and now he wonders, how many ways are there to choose x and y so the deck he will get after removing x cards from the top and y cards from the bottom is valid?
"""
from collections import defaultdict
from sys import stdin, stdout


def get_primes():
    n = 4*(10**4)
    sieve = [1]*(n+1)
    sieve[0], sieve[1] = 0, 0
    nums = []
    for i in range(2, int(n**(0.5))+1):
        if sieve[i] == 1:
            nums.append(i)
            for j in range(i, n//i+1):
                sieve[i*j] = 0
                
    for i in range(int(n**(0.5))+1, len(sieve)):
        if sieve[i] == 1:
            nums.append(i)
    
    """for i,s in enumerate(sieve):
        if s == 1:
            nums.append(i)"""
    return nums


def get_fact_map(n, primes):
    a = n
    hmap = defaultdict(int)
    j = 0
    while n > 1:
        while n % primes[j] == 0:
            n = n//primes[j]
            hmap[primes[j]] += 1
        j += 1
        if j >= len(primes):
            hmap[a] += 1
            break
    return hmap


def remove_num_factors(nmap, vmap):
    for k, v in nmap.items():
        vmap[k] -= v
    return vmap


def add_num_factors(nmap, vmap):
    for k, v in nmap.items():
        vmap[k] += v
    return vmap


def is_divisible(vq, vp):
    for k, v in vp.items():
        if vq[k] < v:
            return False
    return True


if __name__ == "__main__":
    n, k = map(int, stdin.readline().strip().split())
    arr = list(map(int, stdin.readline().strip().split()))
    primes = get_primes()
    vp = get_fact_map(k, primes)
    vq = defaultdict(int)
    arrmap = [defaultdict(int)]*n
    i, j = 0, 0
    res = 0
    while i < n and j < n:
        arrmap[i] = get_fact_map(arr[i], primes)
        vq = add_num_factors(arrmap[i], vq)
        while is_divisible(vq, vp) and j <= i:
            res += n-i
            vq = remove_num_factors(arrmap[j], vq)
            j += 1
        i += 1
    j += 1
    while j < n:
        vq = remove_num_factors(arrmap[j], vq)
        if is_divisible(vq, vp):
            res += n-i
        j += 1
    stdout.write(str((res)))
    
    
    
