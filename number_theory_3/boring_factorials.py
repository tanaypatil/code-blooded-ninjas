"""
Boring Factorials
Send Feedback
Sameer and Arpit want to overcome their fear of Maths and so they have been recently practicing Maths problems a lot. Aman, their friend has been helping them out. But as it goes, Sameer and Arpit have got bored of problems involving factorials. Reason being, the factorials are too easy to calculate in problems as they only require the residue modulo some prime and that is easy to calculate in linear time. So to make things interesting for them, Aman - The Mathemagician, gives them an interesting task. He gives them a prime number P and an integer N close to P, and asks them to find N! modulo P. He asks T such queries.
"""



def power(x, y, p):
    res = 1
    x = x%p
    while y > 0:
        if (y & 1):
            res = (res*x)%p
        y = y >> 1
        x = (x*x)%p
    return res


def mod_inverse(x, p):
    return power(x, p-2, p)


def mod_factorial(n, p):
    if n >= p:
        return 0
    
    res = p-1
    for i in range(n+1, p):
        res = (res * mod_inverse(i, p))%p
    return res


if __name__ == "__main__":
    tc = int(input())
    for t in range(tc):
        n, p = map(int, input().strip().split())
        print(mod_factorial(n, p))
