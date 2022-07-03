import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, h):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n) and visited[nx][ny] == 0 and \
           G[nx][ny] > h:
            visited[nx][ny] = 1 
            dfs(nx, ny, h)

n = int(input())
G = [list(map(int, input().split())) for _ in range(n)]
result = 1

for k in range(max(map(max, G))):
    count = 0
    visited = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j] > k and visited[i][j] == 0:
                visited[i][j] = 1
                count += 1
                dfs(i, j, k)
    result = max(result, count)

print(result)