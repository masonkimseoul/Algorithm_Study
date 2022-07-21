import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]
def dfs(y, x):
    if x == n - 1 and y == m - 1:
        return 1

    if check[y][x] != -1:
        return check[y][x]

    check[y][x] = 0

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[ny][nx] < graph[y][x]:
                check[y][x] += dfs(ny, nx)

    return check[y][x]

m, n = map(int, input().split())
# input
graph = [list(map(int, input().split())) for _ in range(m)]
check = [[-1 for _ in range(n)] for __ in range(m)]
print(dfs(0, 0))
