import sys
from collections import deque

M,N,K=map(int,sys.stdin.readline().split())
graph=[[1]*N for i in range(M)]
visited=[[0]*N for i in range(M)]

for i in range(K):
    ax,ay,bx,by=map(int, sys.stdin.readline().split())
    for j in range(ax,bx):
        for l in range(ay,by):
            graph[l][j]=0

dx=[1,-1,0,0]
dy=[0,0,1,-1]
result=[]
def BFS(x,y):
    queue=deque()
    queue.append([x,y])
    cnt=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and visited[ny][nx]==0 and graph[ny][nx]==1:
                cnt+=1
                visited[ny][nx]=1
                queue.append([nx,ny])
    return cnt

for y in range(M):
    for x in range(N):
        if graph[y][x]==1 and visited[y][x]==0:
            visited[y][x]=1
            result.append(BFS(x,y))

result.sort()
print(len(result))
print(*result)