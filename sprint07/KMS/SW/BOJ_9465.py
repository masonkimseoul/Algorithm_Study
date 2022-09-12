import sys
input = sys.stdin.readline
t = int(input())

for i in range(t):
    L1 =[]
    L2 = []
    n = int(input())
    dp = [[0] * 3 for _ in range(n+1)];
    L1 = list(map(int, input().split()))
    L2 = list(map(int, input().split()))
    dp[0][0] = 0
    dp[0][1] = 0
    dp[0][2] = 0
    dp[1][0] = 0
    dp[1][1] = L1[0] 
    dp[1][2] = L2[0]
    for j in range(1,n):
        dp[j+1][0] = max(dp[j][1],dp[j][2])
        dp[j+1][1] = max(L1[j] + dp[j][2], L1[j] + dp[j][0])
        dp[j+1][2] = max(L2[j] + dp[j][1], L2[j] + dp[j][0])
    print(max(dp[n][1],dp[n][2]))