from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int, input().split()))
S = 0
SS = []
for i in range(1,n+1):
    tmp = list(combinations(L, i))
    for j in tmp:
        SS.append(sum(j))
SS = list(set(SS))
SS.sort()

index = 1
for i in SS:
    if i != index:
        break
    else:
        index+=1
print(index)
