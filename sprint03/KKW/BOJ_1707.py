import sys
from collections import deque

def BFS():
    arr=[0]*(V+1)
    queue=deque()
    for i in range(1,V+1):
        if arr[i]:
            continue
        arr[i]=1
        queue.append(i)
        while queue:
            x=queue.popleft()
            for j in graph[x]:
                if arr[j] and arr[x]==arr[j]:
                    print("NO")
                    return 0
                if arr[j]:
                    continue
                queue.append(j)
                arr[j]=3-arr[x]
    print("YES")


T=int(sys.stdin.readline())
for _ in range(T):
    V,E=map(int, sys.stdin.readline().split())
    graph=[[] for i in range(V+1)]

    for j in range(E):
        va,vb=map(int, sys.stdin.readline().split())

        graph[va].append(vb)
        graph[vb].append(va)
    BFS()