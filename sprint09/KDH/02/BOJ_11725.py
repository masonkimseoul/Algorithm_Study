# 1. visited 유
# import sys
# sys.setrecursionlimit(10000000)
# input = sys.stdin.readline

# N = int(input())

# parents = [-1] * (N+1)
# graph = [[] for _ in range(N+1)]
# visited = [False] * (N+1)

# for _ in range(N-1):
#     n1, n2 = map(int, input().split())
#     graph[n1].append(n2)
#     graph[n2].append(n1)

# def dfs(v):
#     visited[v] = True
#     for node in graph[v]:
#         if not visited[node]:
#             parents[node] = v
#             dfs(node)
# dfs(1)
# print(*parents[2:], sep = "\n")

# 2. visited 무
import sys
from collections import deque
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N = int(input())

parents = [-1] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

def dfs(v):
    stack = deque([v])
    while stack:
        x = stack.pop()
        for node in graph[x]:
            if parents[node] == -1:
                stack.append(node)
                parents[node] = x
dfs(1)
print(*parents[2:], sep = "\n")


