import sys
input = sys.stdin.readline

c = int(input())
n = int(input())

graph = [[] for _ in range(c+1)]
visited = [0] * (c+1)

for _ in range(n):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)


def dfs(node):
    visited[node] = 1
    for i in graph[node]:
        if not visited[i]:
            dfs(i)


dfs(1)
print(sum(visited)-1)
