import sys
input = sys.stdin.readline

n = int(input())

triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

dp = [triangle[0]]
for _ in range(2, n+1):
    dp.append([0 for __ in range(_)])

for i in range(n-1):
    for j in range(i+1):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + triangle[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1])

print(max(dp[n-1]))
        