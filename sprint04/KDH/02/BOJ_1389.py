from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    p1, p2 = map(int, input().split())
    graph[p1].append(p2)
    graph[p2].append(p1)


def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        p1 = queue.popleft()
        for p2 in graph[p1]:
            if checked[p2] == 0:
                checked[p2] = checked[p1] + 1
                queue.append(p2)
    return sum(checked)


min_ = 50000
res = []
for i in range(1, n+1):
    checked = [0] * (n+1)
    checked[i] = 1
    res.append(bfs(i))

print(res.index(min(res))+1)

# 01
# from collections import deque
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# graph = [[] for _ in range(n+1)]

# for _ in range(m):
#     p1, p2 = map(int, input().split())
#     graph[p1].append(p2)
#     graph[p2].append(p1)


# def bfs(x):
#     queue = deque()
#     queue.append(x)
#     while queue:
#         p1 = queue.popleft()
#         for p2 in graph[p1]:
#             if checked[p2] == 0:
#                 checked[p2] = checked[p1] + 1
#                 queue.append(p2)
#     return sum(checked)


# min_ = 50000
# ans = 0
# for i in range(1, n+1):
#     checked = [0] * (n+1)
#     checked[i] = 1
#     res = bfs(i)
#     if min_ > res:
#         min_ = res
#         ans = i

# print(ans)
