import sys
from collections import deque

T=int(sys.stdin.readline())
for _ in range(T):
    N,M=map(int,sys.stdin.readline().split())
    docq=deque(map(int,sys.stdin.readline().split()))
    index=deque(range(N))
    cnt=0
    maxPriority = max(docq)
    while docq:
        tmp=docq.popleft()
        if maxPriority==tmp:
            cnt+=1
            if len(docq)!=0:
                maxPriority=max(docq)
            if M==index.popleft():
                break
        else:
            index.append(index.popleft())
            docq.append(tmp)
    print(cnt)