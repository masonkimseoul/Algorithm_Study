import sys
from collections import deque, defaultdict

def BFS(familyEdge, start, end):
    visited=[]
    queue=deque()
    queue.append((0,start))

    while queue:
        cnt, ptr=queue.popleft()
        visited.append(ptr)
        if ptr==end:
            return cnt
        for j in familyEdge[ptr]:
            if j not in visited:
                visited.append(j)
                queue.append((cnt+1, j))

N=int(sys.stdin.readline())
x,y=map(int, sys.stdin.readline().split())
M=int(sys.stdin.readline())
familyEdge=defaultdict(set)

for i in range(M):
    parent, child=map(int, sys.stdin.readline().split())
    familyEdge[parent].add(child)
    familyEdge[child].add(parent)

print(BFS(familyEdge,x,y))