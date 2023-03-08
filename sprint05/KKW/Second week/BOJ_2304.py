import sys

N=int(sys.stdin.readline())
sum=0
heightMax=1
lengthMax=0
lst=[]
idx=0
for i in range(N):
    L,H=map(int,sys.stdin.readline().split())
    lst.append([L,H])
    if lengthMax<L:
        lengthMax=L
    if heightMax<H:
        heightMax=H
        idx=L
answer=[0]*(lengthMax+1)

for L,H in lst:
    answer[L]=H
tmp=0
for i in range(idx+1):
    if answer[i]>tmp:
        tmp=answer[i]
    sum+=tmp
tmp=0
for i in range(lengthMax,idx,-1):
    if answer[i]>tmp:
        tmp=answer[i]
    sum+=tmp
print(sum)