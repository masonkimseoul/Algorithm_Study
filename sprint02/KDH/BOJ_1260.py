from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for g in graph:
    g.sort()


def dfs(node):
    visited[node] = True
    print(node, end=" ")
    for i in graph[node]:
        if not visited[i]:
            dfs(i)


def bfs(node):
    visited = [False] * (N+1)
    queue = deque([node])
    visited[node] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(V)
print("")
bfs(V)
