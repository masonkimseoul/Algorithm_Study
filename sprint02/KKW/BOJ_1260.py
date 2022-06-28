import sys
from collections import deque

def DFS(graph, node, visitedNode):
    if node not in visitedNode:
        visitedNode.append(node)
    else:
        return

    for j in sorted(graph[node]):
        if j not in visitedNode:
            DFS(graph,j,visitedNode)

def BFS(graph, node, visitedNode):
    queue=deque([node])
    while queue:
        tmp=queue.popleft()
        if tmp not in visitedNode:
            visitedNode.append(tmp)
        for j in sorted(graph[tmp]):
            if j not in visitedNode:
                queue.append(j)

N,M,V=map(int,sys.stdin.readline().split())
graph=[[]*N for i in range(N+1)]
visitedNode=[]
for i in range(M):
    a,b=map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

DFS(graph, V - 1, visitedNode)
print(" ".join(str(i+1) for i in visitedNode))
visitedNode.clear()
BFS(graph, V - 1, visitedNode)
print(" ".join(str(i+1) for i in visitedNode))