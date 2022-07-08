n = int(input())
graph = []
visited = [[0]*n for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, input())))



name =2
def dfs(x,y):
    global cnt
    global n
    global name
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if graph[x][y] == 1:
        cnt = cnt +1
        visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위를 넘었을 때
        if(nx < 0 or ny < 0 or nx >= n or ny >= n):
            continue
        if(graph[nx][ny] != 1):
            continue
        else:
            graph[nx][ny] = name
            if(visited[nx][ny]== 0):
                visited[nx][ny] = 1
                cnt = cnt +1
                dfs(nx,ny)
                
                
result = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == 1:
            name = name+1
            cnt = 0
            dfs(i,j)
            result.append(cnt)
            
        
print(name-2)   

result.sort()
for i in result:
    print(i)


