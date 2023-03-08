from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)

    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)

    def bfs(v):
        q = deque()
        q.append(v)
        while q:
            x = q.popleft()
            for node in graph[x]:
                if node != v and visited[node] == 0:
                    q.append(node)
                    visited[node] = visited[x] + 1
    bfs(1)
    print(visited)

    return visited.count(max(visited))
