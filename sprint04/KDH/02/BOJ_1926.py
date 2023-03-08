from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

count_ = 0
max_ = 0

moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def bfs(i, j):
    queue = deque()
    queue.append([i, j])
    graph[i][j] = 0
    area = 1
    while queue:
        x, y = queue.popleft()
        for move in moves:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    queue.append([nx, ny])
                    graph[nx][ny] = 0
                    area += 1
    return area


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            count_ += 1
            max_ = max(max_, bfs(i, j))

print(count_)
print(max_)
