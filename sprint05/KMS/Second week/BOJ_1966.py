from collections import deque


q = deque()
N = int(input())
for i in range(N):
    cnt = 1
    a , b = map(int, input().split())
    q = deque()
    qindex = deque()
    L = list(map(int, input().split(' ')))
    index = 0
    
    for j in L:
        q.append(j)
        qindex.append(index)
        index +=1
    M = max(q)
    while True:
        if not q:
            break
        tmp = q.popleft()
        index = qindex.popleft()
        if tmp >= M:
            if index == b:
                print(cnt)
                break
            if q:
                M = max(q)
            cnt+=1
        else:
            q.append(tmp)
            qindex.append(index)