import sys

N=int(sys.stdin.readline())
dp=[1,3]
for i in range(2,N):
    dp.append((dp[i-1]+dp[i-2]*2)%10007)
print(dp[N-1])