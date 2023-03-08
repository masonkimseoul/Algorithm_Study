from collections import deque

n, m=map(int, input().split())
mp=[[int(i) for i in input()] for _ in range(n)]
dist=[[[0, 0] for _ in range(m)] for _ in range(n)]
dx=[-1, 0, 0, 1]
dy=[0, -1, 1, 0]

dist[0][0][0]=1
q=deque()
q.append((0, 0, 0))

while q :
    x, y, z=q.popleft()
    for i in range(4) :
        nx, ny=x+dx[i], y+dy[i]
        if(nx<0 or nx>=n or ny<0 or ny>=m) :
            continue
        if(mp[nx][ny]==0 and dist[nx][ny][z]==0) :
            dist[nx][ny][z]=dist[x][y][z]+1
            q.append((nx, ny, z))
        if(z==0 and mp[nx][ny]==1 and dist[nx][ny][1]==0) :
            dist[nx][ny][1]=dist[x][y][0]+1
            q.append((nx, ny, 1))

a=dist[-1][-1][0]
b=dist[-1][-1][1]
if(a!=0 and b!=0) :
    print(min(a, b))
elif(a==0 and b==0) :
    print(-1)
else :
    print(max(a, b))