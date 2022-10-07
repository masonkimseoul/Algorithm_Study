import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(i, j):
    graph[i][j] = 0
    
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1:
                dfs(nx, ny)
    
    

for _ in range(T):
    M, N, K = map(int, input().split())
    
    graph = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
        
    
    