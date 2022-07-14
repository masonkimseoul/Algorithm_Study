from collections import deque
import copy
N,M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]
def BFS(a,b):
    visited = [[(0,0)] * M for i in range(N)]
    q = deque()
    # 벽을 부순적이 있는지 확인하는 비트
    c = 0
    q.append((a,b,c))
    visited[a][b]= (1,0)
    # print(visited)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y, c = q.popleft()
        # print('______')
        # print('x : ', x, 'y :' ,y ,'c :', c)   
        # for i in visited:
        #     print(i)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nc = c
            # print(' nx : ', nx, 'ny :' ,ny ,'nc :', nc)   
            f,d = visited[x][y]
            # print(f,d)
            # 범위에서 벗어날때
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            a,b = visited[nx][ny]
            # print('a :',a, 'b :', b)
            # 1일때
            if matrix[nx][ny] == 1:
                # 뚫은적이 없는경우
                if a == 0 and b == 0 and nc == False:
                    nc = 1
                    q.append((nx,ny,nc))
                    a = f+1
                    visited[nx][ny] = (a,b)
                else:
                    continue
            # 0일때
            elif matrix[nx][ny] == 0:
                if(a == 0):
                    q.append((nx,ny,nc))
                    a = f+1
                    b = nc
                    visited[nx][ny] = (a,b)
                if(a!=0 and b==1 and nc ==False):
                    q.append((nx,ny,nc))
                    a = f+1
                    b = nc
                    visited[nx][ny] = (a,b)
        if x == N-1 and y == M-1:
            a,b = visited[x][y]
            return a
    return -1
                
    

print(BFS(0,0))
