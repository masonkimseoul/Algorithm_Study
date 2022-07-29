from collections import deque


y, x, k = map(int, input().split())
matrix = [[0 for _ in range(x)] for _ in range(y)]
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split(' '))
    
    for xx in range(x1, x2):
        for yy in range(y1, y2):
            matrix[yy][xx] = 1
visit = [[0 for _ in range(x+1)] for _ in range(y+1)]

def bfs(dx,dy):
    global count
    q = deque()
    q.append((dx,dy))
    matrix[dy][dx] = 1
    cx = [1,-1,0,0]
    cy = [0,0,1,-1]
    while q:
        dx,dy = q.popleft()
        for i in range(4):
            rx = cx[i] + dx
            ry = cy[i] + dy
            if 0 <= rx < x and 0 <= ry < y and matrix[ry][rx] == 0:
                matrix[ry][rx] = 1
                q.append((rx,ry))
                count += 1
cnt = []
area = 0
count = 1
for i in range(x):
    for j in range(y):
        if matrix[j][i] == 0:
            area +=1
            bfs(i,j)
            cnt.append(count)
            count =1
            

print(area)
cnt.sort()
for i in cnt:
    print(i, end= " ")