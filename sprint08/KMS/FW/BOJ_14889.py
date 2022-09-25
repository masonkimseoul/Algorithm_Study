from itertools import combinations
import sys
from tkinter import N
input = sys.stdin.readline
n = int(input())
table = []
for i in range(n):
    table.append(list(map(int, input().split())))
all = [_ for _ in range(1,n+1)]
team = list(combinations(all,n//2))
size = len(team)
min = 999999
score = 0
team.sort()
for i in range(size//2):
    teama = 0
    teamb = 0
    for j in range(len(team[i])-1):
        for k in range(j+1, len(team[i])):
            teama += table[team[i][j]-1][team[i][k]-1] + table[team[i][k]-1][team[i][j]-1]
    for j in range(len(team[size-i-1])-1):
        for k in range(j+1, len(team[size-i-1])):
            teamb += table[team[size-i-1][j]-1][team[size-i-1][k]-1] + table[team[size-i-1][k]-1][team[size-i-1][j]-1]        
    if teama < teamb:
        score = teamb - teama
    else:
        score = teama - teamb
    if min > score:
        min = score
print(min)