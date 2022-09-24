from itertools import combinations
import sys
from tkinter import N
input = sys.stdin.readline
n = int(input())
L = []
all = [_ for _ in range(1,n+1)]
team = set(combinations(all,n//2))
b_team = {}
b = 0 
for i in team:
    a = 0
    b |= (1<<5) -1
    for j in i:
        print(j)
        a |= (1 << j)
        b &= ~(1 << j)
    print(a,b)
    # for k in all:
    #     print(k)
    #     n ^= (1 << k)
    # print(n)
        

# link_team = 0
# start_team = 0


# Mini = 100 * n