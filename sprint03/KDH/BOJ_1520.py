import sys
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * (N) for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x == M-1 and y == N-1:
        return 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] < graph[x][y]:
                visited[x][y] += dfs(nx, ny)
    return graph[x][y]


print(visited)
print(dfs(0, 0))
