import sys
input = sys.stdin.readline

N = int(input())
matrix_ = [list(map(int, input().split())) for _ in range(N)]
res = [[0] * N for _ in range(N)]

def dfs(start, i):
    for j in range(N):
        if res[start][j] == 0 and matrix_[i][j] == 1:
            res[start][j] = 1
            dfs(start, j)

for i in range(N):
    dfs(i, i)

for _ in res:
    print(*_, sep = " ")
