import sys
input = sys.stdin.readline
INF = 1000 * 1000 +1
n = int(input())
L =[]
for i in range(n):
    L.append(list(map(int, input().split())))
    
ans = INF


for i in range(3):
    dp = [[INF] * (n) for _ in range(n)]
    dp[0][i] = L[0][i]
    for j in range(1,n):
        dp[j][0] = L[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = L[j][1] + min(dp[j-1][2], dp[j-1][0])
        dp[j][2] = L[j][2] + min(dp[j-1][1], dp[j-1][0])
    for k in range(3):
        if i != k:
            ans = min(ans,dp[-1][k])
print(ans)

