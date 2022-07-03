
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))

visited = [[0] * m for _ in range(n)]
visited[0][0] = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(idx1, idx2):
    queue = deque()
    queue.append([idx1, idx2])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == '1' and visited[nx][ny] == 0:
                    queue.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1


bfs(0, 0)
print(visited[n-1][m-1])
