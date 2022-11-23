import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(input().rstrip()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt 
    visited[x][y] = True
    queue = deque([[x, y]])
    while queue:
        dot = queue.popleft()
        for i in range(4):
            nx = dot[0]+dx[i]
            ny = dot[1]+dy[i]
            # 시작점으로 돌아왔다면
            if nx == x and ny == y and cnt >= 4:
                # print(visited)
                return "Yes"
            elif 0<= nx < N and 0<= ny < M and not visited[nx][ny] and board[nx][ny] == board[x][y]:
                visited[nx][ny] = True
                queue.append([nx, ny])
                cnt += 1
        
    return "No"


res = "No"
for i in range(N):
    for j in range(M):
        visited = [[False] * M for _ in range(N)]
        global cnt
        cnt = 0
        res = dfs(i, j)
        if res == "Yes":
            print(visited)
            break

    if res == "Yes":
        break

print(res)