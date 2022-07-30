from collections import deque

def solution(n, edge):
    answer = 0
    
    graph = [[] for i in range(n + 1)]
    visited = [0 for i in range(n + 1)]
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    
    
    def bfs():
        queue = deque()
        queue.append(1)
        visited[1] = 1    

        while queue:
            n = queue.popleft()
            for i in graph[n]:
                if visited[i] == 0:
                    queue.append(i)
                    visited[i] = visited[n] + 1
    
    bfs()
    max_ = max(visited)

    for i in visited:
        if i == max_:
            answer += 1

    
    return answer