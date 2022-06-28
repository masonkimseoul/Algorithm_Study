def DFS(graph, node, visitedNode, n):
    if node not in visitedNode:
        visitedNode.append(node)
    else:
        return

    for j in range(n):
        if j not in visitedNode and graph[node][j]==1 and node!=j:
            DFS(graph, j, visitedNode, n)

def solution(n, computers):
    answer=0
    visitedNode=[]
    for i in range(n):
        if i in visitedNode:
            continue
        DFS(computers, i, visitedNode, n)
        answer+=1
    return answer

computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(3,computers))