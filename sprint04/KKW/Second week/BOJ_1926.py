import sys
from collections import deque
R,C=map(int, sys.stdin.readline().split())
graph=[]
visited=[[0]*C for i in range(R)]
for i in range(R):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx=[1,-1,0,0]
dy=[0,0,1,-1]
result=[]

def BFS(x,y):
    queue=deque()
    queue.append([x,y])
    cnt = 1
    while queue:
        x,y=queue.popleft()
        for i in  range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=ny<R and 0<=nx<C and visited[ny][nx]==0 and graph[ny][nx]==1:
                cnt+=1
                visited[ny][nx]=1
                queue.append([nx,ny])
    return cnt

for y in range(R):
    for x in range(C):
        if graph[y][x]==1 and visited[y][x]==0:
            visited[y][x]=1
            result.append(BFS(x,y))

print(len(result))
if len(result)==0:
    print(0)
else:
    print(max(result))