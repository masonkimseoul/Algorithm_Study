from collections import deque

def solution(maps):
    queue=deque([(0,0)])
    dx,dy=[-1,1,0,0],[0,0,-1,1]

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny]==1:
                maps[nx][ny]=maps[x][y]+1
                queue.append((nx,ny))
    return maps[-1][-1] if maps[-1][-1]>1 else -1