import sys
from collections import deque

N=int(sys.stdin.readline())
map=[]
for i in range(N):
    tmp=[int(j) for j in sys.stdin.readline()]
    map.append(tmp)

def bfs(cor, map, isVisited):
    direction=[(1,0),(-1,0),(0,1),(0,-1)]
    queue=deque()
    queue.append(cor)
    cnt=0

    while queue:
        y,x=queue.popleft()

        if isVisited[y][x]==0:
            isVisited[y][x]=1
            cnt+=1

            for dir in direction:
                ny, nx=y+dir[0],x+dir[1]

                if nx>=0 and nx<N and ny>=0 and ny<N and isVisited[ny][nx]==0 and map[ny][nx]==1:
                    ncor=(ny,nx)
                    queue.append(ncor)
    return cnt

isVisited=[[0 for i in range(N)] for j in range(N)]
cnt=0
answer=[]

for y in range(N):
    for x in range(N):
        if isVisited[y][x]==0 and map[y][x]==1:
            cnt+=1
            cor=(y,x)
            answer.append(bfs(cor,map,isVisited))
answer.sort()
print(cnt)
print("\n".join([str(i) for i in answer]))