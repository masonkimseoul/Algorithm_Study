# dfs
# def dfs(computers, node, visited):
#     visited[node] = True
#     for i in range(len(computers[node])):
#         if computers[node][i] == 1 and not visited[i]:
#             dfs(computers, i, visited)


# def solution(n, computers):
#     answer = 0
#     visited = [False] * (n)

#     for i in range(n):
#         if not visited[i]:
#             dfs(computers, i, visited)
#             answer += 1
#     return answer

# bfs
from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False] * (n)

    def bfs(computers, v, visited):
        queue = deque([v])
        visited[v] = True
        while queue:
            x = queue.popleft()
            for i in range(len(computers)):
                if computers[x][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

    for v in range(n):
        if not visited[v]:
            bfs(computers, v, visited)
            answer += 1
    return answer
