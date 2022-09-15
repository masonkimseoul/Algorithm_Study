import sys, math
input = sys.stdin.readline

N = int(input())

dp = [i for i in range(N+1)]
for i in range(1,int(math.sqrt(N)+1)):
    dp[i**2] = 1
print(dp)