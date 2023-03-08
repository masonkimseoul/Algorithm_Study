# 02.
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input().rstrip()))
visited = set()


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

max_ = -1


def dfs(x, y):
    global max_

    max_ = max(max_, len(visited))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if board[nx][ny] not in visited:
                visited.add(board[nx][ny])
                dfs(nx, ny)
                visited.remove(board[nx][ny])


visited.add(board[0][0])
dfs(0, 0)
print(max_)

# 01.
# import sys
# input = sys.stdin.readline


# R, C = map(int, input().split())
# board = [list(input().rstrip()) for _ in range(R)]
# visited = [[False]*C for _ in range(R)]
# passed = []

# cnt = 1

# # 왼, 오, 위, 아래
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# max_ = -1


# def dfs(x, y):
#     visited[x][y] = True
#     passed.append(board[x][y])

#     global max_

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < R and 0 <= ny < C:
#             if board[nx][ny] not in passed:
#                 dfs(nx, ny)

#     # print(board[x][y], passed)
#     max_ = max(max_, len(passed))
#     passed.pop()
#     # print(passed)
#     return


# dfs(0, 0)
# print(max_)
