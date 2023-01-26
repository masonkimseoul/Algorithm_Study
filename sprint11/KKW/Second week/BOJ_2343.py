import sys
N,M=map(int,sys.stdin.readline().split())
numbers=list(map(int,sys.stdin.readline().split()))

start, end = max(numbers), sum(numbers)
answer=0
while start<=end:
    mid=(start+end)//2
    tmp=0
    cnt=1
    for i in range(N):
        tmp+=numbers[i]
        if tmp>mid:
            cnt+=1
            tmp=numbers[i]
    if cnt<=M:
        answer=mid
        end=mid-1
    else:
        start=mid+1
print(answer)