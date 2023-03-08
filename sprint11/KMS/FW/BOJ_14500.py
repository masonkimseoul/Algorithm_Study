n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]

R = []


def DFS(x, y, result, cnt):
    visit[x][y] = 1
    if cnt == 4:
        R.append(result)
        visit[x][y] = 0
        return
    else:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                DFS(nx, ny, result+graph[nx][ny], cnt + 1)
                visit[nx][ny] = 0


for i in range(n):
    for j in range(m):
        DFS(i, j, graph[i][j], 1)
        visit[i][j] = 0

        if i == 0 and j == 0:
            continue
        if i == 0 and j == m-1:
            continue
        if i == n-1 and j == 0:
            continue
        if i == n-1 and j == m-1:
            continue
        # ㅗ
        if 0 <= i+1 < n and 0 <= j-1 < m and 0 <= j+1 < m:
            R.append(graph[i][j] + graph[i+1][j-1] +
                     graph[i+1][j] + graph[i+1][j+1])
        # ㅏ
        if 0 <= i + 1 < n and 0 <= i - 1 < n and 0 <= j-1 < m:
            R.append(graph[i][j] + graph[i][j-1] +
                     graph[i+1][j-1] + graph[i-1][j-1])
        # ㅜ
        if 0 <= i-1 < n and 0 <= j+1 < m and 0 <= j-1 < m:
            R.append(graph[i][j] + graph[i-1][j] +
                     graph[i-1][j+1] + graph[i-1][j-1])
        # ㅓ
        if 0 <= j+1 < m and 0 <= i+1 < n and 0 <= i-1 < n:
            R.append(graph[i][j] + graph[i][j+1] +
                     graph[i+1][j+1] + graph[i-1][j+1])
R.sort()
# print(R)
print(R[-1])


# 5 5
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 9 9 1
# 1 1 8 9 9
# 1 1 1 1 1
