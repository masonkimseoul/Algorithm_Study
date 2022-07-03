'''
    BFS 버전
'''

from collections import deque
import queue

if __name__ == "__main__":
    
    def bfs(idx_y, idx_x):
        
        queue = deque()
        box = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        queue.append([idx_y, idx_x])

        while queue:
            id_y, id_x = queue.popleft()
            matrix[id_y][id_x] = 0

            for i in box:
                y = id_y + i[0]
                x = id_x + i[1]
                if (x >= 0 and x < M and y >= 0 and y < N and (matrix[y][x] == 1)):
                    queue.append([y, x])


    num = int(input())

    for k in range(num):
        
        M, N, K = map(int, input().split())
        matrix = [[0 for i in range(M)] for j in range(N)]
        count = 0
        
        for i in range(K):
            a, b = map(int, input().split())
            matrix[b][a] = 1
    
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 1:
                    bfs(i, j)
                    count += 1
        
        print(count)
