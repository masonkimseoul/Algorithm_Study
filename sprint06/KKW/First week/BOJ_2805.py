import sys

N,M=map(int, sys.stdin.readline().split())

tree=list(map(int, sys.stdin.readline().split()))
minH=0
maxH=max(tree)
answer=0
while maxH>=minH:
    cnt=0
    midH=(minH+maxH)//2

    for i in tree:
        if i>midH:
            cnt+=i-midH
        if cnt>=M:
            break
    if cnt>=M:
        answer=max(answer,midH)
        minH=midH+1
    else:
        maxH=midH-1
print(answer)