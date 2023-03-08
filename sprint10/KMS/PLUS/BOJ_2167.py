import sys
n, m = map(int, input().split())
L = [(list(map(int, input().split()))) for _ in range(n)]


k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    S = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            S += L[a][b]
    print(S)
