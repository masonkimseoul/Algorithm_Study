import sys
from collections import deque

def BFS():
    while queue:
        X,Y=queue.popleft()
        for i in range(len(location)):
            dx=X+location[i][0]
            dy=Y+location[i][1]

            if dx>=0 and dx<N and dy>=0 and dy<M:
                if maze[dx][dy]==1:
                    maze[dx][dy]=maze[X][Y]+1
                    queue.append((dx,dy))


N,M=map(int, sys.stdin.readline().split())
maze=[[]*M for _ in range(N)]
for i in range(N):
    maze[i]=list(map(int,sys.stdin.readline().rstrip()))
location=[(-1,0), (1,0), (0,-1), (0,1)]
queue=deque()
queue.append((0,0))

BFS()
print(maze[N-1][M-1])