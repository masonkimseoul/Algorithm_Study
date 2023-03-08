n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[-1] * m for i in range(n)]
def dfs(x,y):
    
    if x == n-1 and y == m-1:
        return 1
    
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    
    if visit[x][y] != -1:
        return visit[x][y]
    
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        #벽을 넘었을 때
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        
        # 방문한 적이 있을경우 
        
        if graph[nx][ny] < graph[x][y]:                
                cnt += dfs(nx,ny)
    visit[x][y] = cnt
    return visit[x][y]
                
                
    
print(dfs(0,0))