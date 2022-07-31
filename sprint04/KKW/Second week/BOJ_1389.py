import sys
import heapq
from collections import deque
N,M=map(int, sys.stdin.readline().split())
dic={i: [] for i in range(1,N+1)}
heap=[]
for j in range(M):
    x,y=map(int, sys.stdin.readline().split())
    dic[x].append(y)
    dic[y].append(x)

for i in range(1,N+1):
    result=0
    cnt=0
    notVisited=deque([i])
    visited=[0]*(N+1)
    visited[i]=1

    while notVisited:
        cnt+=1
        for j in range(len(notVisited)):
            for k in dic[notVisited.popleft()]
                if visited[k]==0:
                    visited[k]=1
                    notVisited.append(k)
                    result+=cnt
    heapq.heappush(heap,[result,i])

print(heap[0][1])