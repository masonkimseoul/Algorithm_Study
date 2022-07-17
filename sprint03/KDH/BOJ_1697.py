from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * (100000+1)


def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        n = queue.popleft()
        if n == K:
            return visited[n]
        for move in (n-1, n+1, n*2):
            if 0 <= move <= 100000 and visited[move] == 0:
                queue.append(move)
                visited[move] = visited[n] + 1


visited[N] = 1
print(bfs(N))
