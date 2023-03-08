from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
L = {}
for _ in range(M):
    a, b = map(int, input().split())
    if b in L:
        L[b].append(a)
    else:
        L[b] = []
        L[b].append(a)


def BFS(start, end):
    q = deque()
    q.append(start)
    visit = [False for _ in range(N + 1)]
    visit[start] = 1
    while q:
        V = q.popleft()
        if V == end:
            return True
        if V in L:
            for i in L[V]:
                if visit[i] == -1:
                    q.append(i)
                    visit[i] = True
    return False


answer = [(0, 0) for _ in range(N+1)]
for i in range(1, N+1):
    cnt = 0
    for j in L:
        if i == j:
            continue
        if BFS(j, i):
            cnt += 1
    answer.append((i, cnt))
answer.sort(key=lambda x: -x[1])
M = answer[0][1]
for i in range(N+1):
    if M > answer[i][1]:
        break
    print(answer[i][0], end=' ')
