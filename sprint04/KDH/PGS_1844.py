from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    visited = [[-1] * m for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs():
        visited[0][0] = 1
        queue = deque()
        queue.append((0, 0))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    if visited[nx][ny] == -1:
                        queue.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1

    bfs()

    return visited[-1][-1]
