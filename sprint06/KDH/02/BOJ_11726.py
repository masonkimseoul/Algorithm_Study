import sys
input = sys.stdin.readline

n = int(input())

dp = [1, 2]

if n >= 3:
    for i in range(3, n+1):
        dp.append(dp[-1] + dp[-2])

print(dp[n-1] % 10007)