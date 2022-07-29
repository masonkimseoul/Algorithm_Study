from collections import deque
def solution(n, edge):
    answer = 0
    V = [[] for i in range(n+1)]
    for i in edge:
        V[i[0]].append(i[1])
        V[i[1]].append(i[0])
    visit = [0 for _ in range(n+1)]
    def bfs():
        q = deque()
        q.append((1,1))
        visit[1] = 1 
        while q:
            start, cnt = q.popleft()
            for i in V[start]:
                if visit[i] == 0:
                    visit[i] = cnt
                    q.append((i, cnt+1))
    bfs()
    m = max(visit)
    answer = visit.count(m)
    print(visit)

    return answer