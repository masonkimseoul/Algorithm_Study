from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))

# 이동
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = '0'
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == '1':
                    queue.append((nx, ny))
                    # 방문 표시
                    graph[nx][ny] = '0'
                    count += 1
    return count


ans = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            ans.append(bfs(i, j))
print(len(ans))
ans.sort()
for num in ans:
    print(num)
