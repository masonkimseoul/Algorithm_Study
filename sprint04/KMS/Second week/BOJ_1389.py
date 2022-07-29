from collections import deque


n, m = map(int, input().split())
matrix = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)
    

def bfs(a,b):
    cnt = 0
    visit = [0] * (n+1)
    q = deque()
    q.append((a,b,1))
    visit[a] = 1
    while q:
        a, b ,cnt= q.popleft()
        for i in matrix[a]:
            if visit[i] == 1:
                continue
            if i == b:
                return cnt
            visit[i] = 1
            q.append((i,b,cnt+1))
            
    return 0
    
cnt = []
for i in range(1,n+1):
    tmp = 0
    for j in range(1,n+1):
        if i == j:
            continue
        tmp += bfs(i,j)
    cnt.append(tmp)
c = min(cnt)
print(cnt.index(c)+1)