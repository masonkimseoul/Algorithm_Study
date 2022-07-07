from collections import deque
n = int(input())
A, B = input().split(' ')
A = int(A)
B = int(B)
e = int(input())
matrix = [[0]*(n+1) for _ in range(n+1)]
visited = [0 for _ in range(n+1)]


for i in range(e):
    x, y = input().split(' ')
    x = int(x)
    y = int(y)
    matrix[x][y] = 1
    matrix[y][x] = 1


answer = -1
def BFS(x,y):
    q = deque()
    q.append((0, x))
    visited[x]= 1
    tmp = 0
    while q:
        d, x = q.popleft()
        if x == y:
            return d
        for i in range(len(matrix[x])):
            if matrix[x][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append((d+1, i))

        tmp += 1
    return -1
print(BFS(A,B))