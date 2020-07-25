"""
Sanchit And Nuclear Reactor
Send Feedback
We all know Sanchit Lee Cooper who is a Caltech theoretical physicist. He has eccentric and arrogant behavior. Due to his belief that he's intellectually superior, he's not ashamed to insult his own friends, like Howard, who is an engineer and not a real scientist. But nobody messes with an engineer. So Howard accepted an challenge from Sanchit. Sanchit was involved in numerous experiments as a wunderkind, such as his plan for building his own nuclear reactor - a plan stopped by government. So Sanchit presented Howard with a problem about his own nuclear reactor. It contains a large tank and at each second an atom is introduced in the tank which reacts with already existing atoms and produces some energy. Also he defined a special threshold number for his reactor called Cooper number m which is always a prime number. Energy output is defined as previous energy output of the tank multiplied by number of atoms present in it. But due to some special condition of the tank, all atoms attains stable state when number of atoms are multiple of Cooper number and no new reaction occurs. Energy output in this case is same as previous case. Also initial energy of the reactor is 1 and initially there is no atom in the tank. Now Sanchit ask Howard to tell the energy output after time T. But sadly Howard is not able to solve it and ask for your help.
"""
from sys import stdin, stdout


if __name__ == "__main__":
    tc = int(stdin.readline())
    for t in range(tc):
        t, m = map(int, stdin.readline().strip().split())
        res, q, r = 1, t//m, t%m
        for i in range(1, r+1):
            res *= ((q*m) + i)%m
        if q % 2 != 0:
            res *= (m-1)
        stdout.write(str(res%m)+"\n")
