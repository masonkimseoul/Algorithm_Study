import sys
input = sys.stdin.readline
n = int(input())
L = [[0]]
for i in range(n):
    L.append([0]+list(map(int, input().split())))
    
    
dp = [[0] * (n+1) for i in range(n+1)]
dp[1][1] = L[1][1]
for i in range(2,n+1):
    dp[i][1] = dp[i-1][1] + L[i][1]
    for j in range(2,i):
        dp[i][j] = max(dp[i-1][j-1] + L[i][j], dp[i-1][j] + L[i][j])
    dp[i][i] = L[i][i] + dp[i-1][i-1]
print(max(dp[n]))