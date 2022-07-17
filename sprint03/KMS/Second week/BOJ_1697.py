import sys
from collections import deque
n,k = map(int, input().split())

visit= []
for i in range(100001):
    visit.append(0)
q = deque()

def bfs(n,k):
    q.append(n)
    visit[n] = 1
    while(q):
        tmp = q.popleft()
        if tmp > 100001 or tmp < 0:
            continue
        if tmp == k:
            return visit[k]        
        if tmp *2 <= 100001 and visit[tmp * 2] == 0:
            visit[tmp *2] = visit[tmp]+1
            q.append(tmp*2)
        if tmp +1 < 100001 and visit[tmp + 1] == 0:
            visit[tmp + 1] = visit[tmp]+1
            q.append(tmp+1)
        if tmp -1 >= 0 and visit[tmp - 1] == 0:
            visit[tmp - 1] = visit[tmp]+1
            q.append(tmp-1)
print(bfs(n,k)-1)
        
