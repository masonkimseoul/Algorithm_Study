import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(x, y):
    graph[x][y] = 0
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0<= nx < w and 0<= ny < h and graph[nx][ny] == 1:
            dfs(nx, ny)

# 1 land, 0 ocean
while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
