import sys

N=int(sys.stdin.readline())
student=int(sys.stdin.readline())
votes=list(map(int,sys.stdin.readline().split()))

cnt=0
idx=0
lst={}
for i in votes:
    if i in lst:
        lst[i][0]+=1
    else:
        if cnt>=N:
            lst=dict(sorted(lst.items(), key=lambda x: (x[1][0],x[1][1])))
            tmp=list(lst.keys())
            lst.pop(tmp[0])
        lst[i]=[1,idx]
        idx+=1
        cnt+=1
result=sorted(list(lst.keys()))
for i in result:
    print(i, end=" ")