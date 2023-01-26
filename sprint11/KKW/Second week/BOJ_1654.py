import sys
K,N=map(int,sys.stdin.readline().split())
length=[]
for i in range(K):
    length.append(int(sys.stdin.readline()))
start,end=1,max(length)
while start<=end:
    mid=(start+end)//2
    answer=0
    for i in length:
        answer+=(i//mid)
    if answer>=N:
        start=mid+1
    else:
        end=mid-1
print(end)