from collections import deque
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]


def BFS(x1, y1, x2, y2, cnt):
    q = deque()
    q.append((x1, y1, x2, y2, cnt))
    while q:
        x1, y1, x2, y2, cnt = q.popleft()
        if cnt >= 10:
            return -1
        # 상 하 좌 우
        nx = [-1, 1, 0, 0]
        ny = [0, 0, -1, 1]
        for i in range(4):
            dx1 = nx[i] + x1
            dy1 = ny[i] + y1
            dx2 = nx[i] + x2
            dy2 = ny[i] + y2
            # 1번 동전이 떨어질 경우 2번은 안에있음
            if (0 <= dx1 < n and 0 <= dy1 < m) and (dx2 < 0 or dx2 >= n or dy2 < 0 or dy2 >= m):
                return cnt + 1
            # 2번 동전이 떨어질 경우 1번은 안에 있음
            if (0 <= dx2 < n and 0 <= dy2 < m) and (dx1 < 0 or dx1 >= n or dy1 < 0 or dy1 >= m):
                return cnt + 1
            # 둘 다 안에 있는 경우
            if 0 <= dx1 < n and 0 <= dy1 < m and 0 <= dx2 < n and 0 <= dy2 < m:
                # 1번이 벽을 만났을 경우 그래도
                if graph[dx1][dy1] == '#':
                    dx1 = x1
                    dy1 = y1
                # 2번이 벽을 만났을 경우 그대로
                if graph[dx2][dy2] == '#':
                    dx2 = x2
                    dy2 = y2
                q.append((dx1, dy1, dx2, dy2, cnt+1))


def find_coinindex(graph):
    coin = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'o':
                coin.append(i)
                coin.append(j)
    return coin


coin = find_coinindex(graph)
x1, y1, x2, y2 = coin
print(BFS(x1, y1, x2, y2, 0))
