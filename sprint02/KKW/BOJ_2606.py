import sys

def dfs(graph, node, visitedNode, cnt):
    cnt=0
    if node not in visitedNode:
        visitedNode.append(node)

    for j in graph[node]:
        if j not in visitedNode:
            cnt+=1
            cnt+=dfs(graph, j, visitedNode, cnt)
    return cnt

computers=int(sys.stdin.readline())
edges=int(sys.stdin.readline())

graph=[[]*computers for i in range(computers+1)]
visitedNode=[]
for i in range(edges):
    a,b=map(int,sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

cnt=0
cnt+=dfs(graph, 0, visitedNode, cnt)
print(cnt)