from collections import deque
def solution(maps):
    answer = 0
    m = len(maps)
    n = len(maps[0])
    print ('n :', n, 'm :', m)
    
    def bfs(x,y):
        q = deque()
        q.append((x,y))
        while q:
            x, y = q.popleft()
            nx = [1, -1 , 0 , 0]
            ny = [0, 0, 1, -1]
            for i in range(4):
                rx = nx[i] + x
                ry = ny[i] + y
                if 0 <= rx < m and 0 <= ry < n and maps[rx][ry] == 1:
                    maps[rx][ry] = maps[x][y] + 1
                    q.append((rx,ry))
            if x == m-1 and y ==n-1:
                return maps[m-1][n-1]
        return -1
    answer = bfs(0,0)
    return answer