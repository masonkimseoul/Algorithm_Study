n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for i in range(n)]

cnt = 0
def dfs(x,y):
    global cnt
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    if x == n-1 and y == m-1:
        cnt+=1
        return    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        #벽을 넘었을 때
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] < graph[x][y] and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            dfs(nx,ny)
            visit[nx][ny] = 0
        else:
            continue
    
dfs(0,0)
print(cnt)