from collections import deque
import sys

global matrix
global M
global N

sys.setrecursionlimit(10 ** 4) # 재귀 깊이 조절

def dfs(idx_y, idx_x):
    check_box = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    for i in check_box:
        x = idx_x + i[0]
        y = idx_y + i[1]
        if ((x >= 0 and x < M and y >= 0 and y < N) and matrix[y][x] == 1):
            matrix[y][x] = 0
            dfs(y, x)


if __name__ == "__main__":
    
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
                    dfs(i, j)
                    count += 1
        
        print(count)

