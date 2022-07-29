from collections import deque
import xdrlib


Y, X = map(int, input().split())
matrix = [list(map(int, input().split(' '))) for _ in range(Y)]
def bfs(x,y):
    global count
    q = deque()
    q.append((x,y))
    matrix[y][x] = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while q:
        x,y = q.popleft()
        for i in range(4):
            rx = dx[i] + x
            ry = dy[i] + y
            if 0 <= rx < X and 0<= ry < Y and matrix[ry][rx] == 1:
                matrix[ry][rx] = 0
                q.append((rx,ry))
                count +=1
cnt = []
count = 0
for xx in range(X):
    for yy in range(Y):
        if matrix[yy][xx] == 1:
            bfs(xx,yy)
            cnt.append(count)
            count = 1
print(len(cnt))
print(max(cnt))