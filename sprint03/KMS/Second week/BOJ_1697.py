from collections import deque
n,k = map(int, input().split())

visit= []
for i in range(100001):
    visit.append(0)
q = deque()

def bfs(a,k):
    global n
    q.append((a,0))
    while(q):
        tmp,cnt = q.pop()
        if tmp > 100001 or 0 > tmp:
            continue
        # print(tmp)
        if tmp == k:
            return cnt
        if visit[tmp * 2] == 0:
            visit[tmp *2] = cnt
            q.append((tmp*2,cnt+1))
        if visit[tmp + 1] == 0:
            visit[tmp + 1] = cnt
            q.append((tmp+1,cnt+1))
        if visit[tmp - 1] == 0:
            visit[tmp - 1] = cnt
            q.append((tmp-1,cnt+1))
        
print(bfs(n,k))
        


# def dfs(a,k,cnt):
#     if a == k:
#         print(a,cnt)
#         return
#     dfs(2*a,k,cnt+1)
#     dfs(a-1,k,cnt+1)
#     dfs(a+1,k,cnt+1)
# dfs(n,k,0)