import sys

N=int(sys.stdin.readline())
dp=[_ for _ in range(N+1)]
for i in range(2,N+1):
    for j in range(2, i//2+1):
        if i<j*j:
            break
        if dp[i]>dp[i-j*j]+1:
            dp[i]=dp[i-j*j]+1
print(dp[N])