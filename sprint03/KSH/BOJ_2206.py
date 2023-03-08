from collections import deque

def bfs(lst, visited):
    
    queue = deque()
    box = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    queue.append([0, 0, 0])
    while queue:
        x, y, wall = queue.popleft()

        if x == (len(lst[0]) - 1) and (y == (len(lst) - 1)):
            return visited[y][x][wall] + 1

        for i in box:
            x_ = x + i[0]
            y_ = y + i[1]
            if (x_>=0 and x_<len(lst[0]) and (y_>=0 and y_<len(lst))):
                # 벽이 없이 그냥 옆으로 이동
                if (lst[y_][x_] == 0 and visited[y_][x_][wall] == 0):
                    queue.append([x_, y_, wall])
                    visited[y_][x_][wall] = visited[y][x][wall] + 1
                # 벽을 뚫고 가는 상황
                if (lst[y_][x_] == 1 and visited[y_][x_][wall] == 0 and wall == 0):
                    queue.append([x_, y_, 1])
                    visited[y_][x_][1] = visited[y][x][wall] + 1
        
    return -1

if __name__ == "__main__":

    lst = []
    n, m = map(int, input().split())
    for i in range(n):
        lst.append(list(map(int, input())))
    # visited = [[0 for i in range(m)] for j in range(n)]
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

    print(bfs(lst, visited))
