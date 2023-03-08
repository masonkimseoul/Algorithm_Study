import sys
from itertools import combinations

N=int(sys.stdin.readline())
humans=list(range(N))
ability=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
teams=list(combinations(list(range(N)),N//2))

abilitySum=[]

for i in range(len(teams)//2):
    tmp=0

    index=i
    for j in teams[index]:
        for k in teams[index]:
            if j==k:
                continue
            tmp+=ability[j][k]

    index=len(teams)-1-i
    for j in teams[index]:
        for k in teams[index]:
            if j == k:
                continue
            tmp -= ability[j][k]

    abilitySum.append(abs(tmp))

print(min(abilitySum))

