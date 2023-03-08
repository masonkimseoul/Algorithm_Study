import sys
input = sys.stdin.readline
n = int(input())
S = 0
for i in range(n):
    L = input().split()
    if L[0] == 'add':
        S |= (1 << int(L[1]))
    if L[0] == 'remove':
        S &= ~(1 << int(L[1]))
    if L[0] == 'check':
        print(1 if S & (1 << int(L[1])) != 0 else 0)
    if L[0] == 'toggle':
        S ^= (1 << int(L[1]))
    if L[0] == 'all':
        S = (1 << 21) - 1
    if L[0] == 'empty':
        S = 0