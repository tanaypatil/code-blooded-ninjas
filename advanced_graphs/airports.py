"""
AIRPORTS
Send Feedback
AIRPORTS
The government of a certain developing nation wants to improve transportation in one of its most inaccessible areas, in an attempt to attract investment. The region consists of several important locations that must have access to an airport.
Of course, one option is to build an airport in each of these places, but it may turn out to be cheaper to build fewer airports and have roads link them to all of the other locations. Since these are long distance roads connecting major locations in the country (e.g. cities, large villages, industrial areas), all roads are two-way. Also, there may be more than one direct road possible between two areas. This is because there may be several ways to link two areas (e.g. one road tunnels through a mountain while the other goes around it etc.) with possibly differing costs.
A location is considered to have access to an airport either if it contains an airport or if it is possible to travel by road to another location from there that has an airport. You are given the cost of building an airport and a list of possible roads between pairs of locations and their corresponding costs. The government now needs your help to decide on the cheapest way of ensuring that every location has access to an airport. The aim is to make airport access as easy as possible, so if there are several ways of getting the minimal cost, choose the one that has the most airports.
"""


## Read input as specified in the question.
## Print output as specified in the question.
import operator
from sys import stdin
from collections import defaultdict


def get_parent(i, parent):
    while i != parent[i]:
        i = parent[i]
    return i
        


if __name__ == "__main__":
    tc = int(input())
    for t in range(tc):
        k = [int(i) for i in input().strip().split()]
        if(len(k) < 3):
        	break
        n, m, a = k
        edges = []
        parent = [i for i in range(n)]
        for i in range(m):
            x, y, w = map(int, input().strip().split())
            x, y = x-1, y-1
            edges.append([x, y, w])
        edges = sorted(edges, key=operator.itemgetter(2))

        cost = 0
        i = 0
        e = 0

        count = 0
        cost = 0
        for i in range(m):
            v1, v2, w = edges[i][0], edges[i][1], edges[i][2]
            if w < a and count < n:
                p1 = get_parent(v1, parent)
                p2 = get_parent(v2, parent)
                if p1 != p2:
                    count += 1
                    cost += w
                    parent[p1] = p2
            else:
                break

        airports = 0
        for i in range(n):
            if parent[i] == i:
                airports += 1
        
        cost += (airports*a)
        print("Case #"+str(t+1)+": "+str(cost)+" "+str(airports))
