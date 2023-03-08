import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
L = [[] for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    L[a].append((b, c))
    L[b].append((a, c))


A, B = map(int, input().split())

for i in range(1, N+1):
    L[i].sort(key=lambda x: x[1], reverse=True)
MAX = max(L[A][0][1], L[A][0][1])


def BFS(start, dest, weight):
    visit = [-1 for _ in range(N+1)]
    q = deque()
    q.append(start)
    visit[start] = 1
    while q:
        t = q.popleft()
        if t == dest:
            return True
        for d, w in L[t]:
            if visit[d] == -1 and w >= weight:
                q.append(d)
                visit[d] = 1
    return False


l = 1
r = MAX
while l <= r:
    weight = (l+r)//2
    if BFS(A, B, weight):
        l = weight + 1
    else:
        r = weight - 1
print(r)
