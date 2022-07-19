import sys
from collections import deque

def BFS(N):
    time=0
    result=deque([[N, time]])
    while result:
        ptr, t=result.popleft()
        if not isVisited[ptr]:
            isVisited[ptr]=True
            if ptr==K:
                return t
            t+=1

            if ptr*2<=100000:
                result.append([ptr*2,t])
            if ptr+1<=100000:
                result.append([ptr+1,t])
            if ptr-1>=0:
                result.append([ptr-1, t])
    return t


N,K=map(int, sys.stdin.readline().split())
isVisited=[False]*100001
print(BFS(N))