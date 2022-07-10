import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
p1, p2 = map(int, input().split())
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

relations = []


def dfs(v):
    for p in graph[v]:
        if visited[p] == 0:
            visited[p] = visited[v] + 1
            dfs(p)


dfs(p1)
if visited[p2] > 0:
    print(visited[p2])
else:
    print(-1)
