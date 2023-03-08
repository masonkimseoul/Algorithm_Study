from collections import deque
import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
board = [[0] * n for _ in range(m)]
rec_pos = [[] for _ in range(k)]
for _ in range(k):
    rec_pos[_] = list(map(int, input().split()))

# -1 방문 불가, 0 방문 가능, 1 방문 완료
for x1, y1, x2, y2 in rec_pos:
    for x in range(x1, x2):
        for y in range(y1+1, y2+1):
            board[m-y][x] = -1

res = []
moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def bfs(i, j):
    cnt = 1
    queue = deque()
    queue.append([i, j])
    board[i][j] = 1
    while queue:
        x, y = queue.popleft()
        for move in moves:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < m and 0 <= ny < n:
                if board[nx][ny] == 0:
                    queue.append([nx, ny])
                    board[nx][ny] = 1
                    cnt += 1
    return cnt


for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            res.append(bfs(i, j))

print(len(res))
print(" ".join(map(str, sorted(res))))
