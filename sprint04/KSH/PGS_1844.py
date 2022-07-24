from collections import deque

def bfs(lst):
    queue = deque()
    visited = [[-1 for i in range(len(lst[0]))] for j in range(len(lst))]
    box = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    queue.append([0, 0])
    visited[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in box:
            x_, y_ = x + i[0], y + i[1]
            if 0<=x_<len(lst[0]) and 0<=y_<len(lst):
                if visited[y_][x_] == -1 and lst[y_][x_] == 1:
                    visited[y_][x_] = visited[y][x] + 1
                    queue.append([x_, y_])
    
    return visited[len(lst)-1][len(lst[0])-1]

def solution(maps):
    answer = 0
    
    answer = (bfs(maps))
    
    return answer