import sys

N=int(sys.stdin.readline())
cnt=0
calcList=[0]*(N+1)

for i in range(2,N+1):
    calcList[i]=calcList[i-1]+1
    if i%2==0:
        calcList[i]=min(calcList[i],calcList[i//2]+1)
    if i%3==0:
        calcList[i]=min(calcList[i],calcList[i//3]+1)

print(calcList[N])