R, C = map(int, input().split())
matrix = [[*map(lambda x: ord(x) - ord('A'), input())] for _ in range(R)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def dfs(x, y, cnt):
    global answer
    answer = max(answer, cnt)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < C and 0 <= ny < R and not visited[matrix[ny][nx]]:
            visited[matrix[ny][nx]] = True
            dfs(nx, ny, cnt + 1)
            visited[matrix[ny][nx]] = False

answer = 0
visited = [False] * 26
visited[matrix[0][0]] = True
dfs(0, 0, 1)
print(answer)