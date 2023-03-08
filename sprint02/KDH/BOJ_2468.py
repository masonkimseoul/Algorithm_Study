import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
graph = [[] for _ in range(n)]

ans = 1
max_height = 1
min_height = 100

for i in range(n):
    graph[i] = (list(map(int, input().split())))
    max_height = max(max(graph[i]), max_height)
    min_height = min(min(graph[i]), min_height)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(idx1, idx2, h):
    visited[idx1][idx2] = True
    for i in range(4):
        nx = idx1 + dx[i]
        ny = idx2 + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] > h:
                dfs(nx, ny, h)


for h in range(min_height, max_height+1):
    visited = [[False] * (n) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > h:
                dfs(i, j, h)
                cnt += 1
    ans = max(ans, cnt)

print(ans)
