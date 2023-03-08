import sys

N=int(sys.stdin.readline())
numList=list(map(int,sys.stdin.readline().split()))
dp=[1]*N

for i in range(N):
    for j in range(i):
        if numList[i]>numList[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))

answer=[]
maxVal=max(dp)
for i in range(N-1,-1,-1):
    if dp[i]==maxVal:
        answer.append(numList[i])
        maxVal-=1
answer.reverse()
print(*answer)