import sys
input = sys.stdin.readline
k = int(input())
L = []
for i in range(k):        
    L.append(int(input()))

N = max(L)
dp = [[0] * (4) for _ in range(N+1)]
dp[1][1] = 1
dp[2][2] = 1
dp[3][3] = 1
dp[3][1] = 1
dp[3][2] = 1
if N > 3:
    for j in range(4,N+1):
        dp[j][1] = (dp[j-1][2] + dp[j-1][3])%1000000009
        dp[j][2] = (dp[j-2][1] + dp[j-2][3])%1000000009
        dp[j][3] = (dp[j-3][1] + dp[j-3][2])%1000000009
for i in L:
    print(sum(dp[i])%1000000009)

