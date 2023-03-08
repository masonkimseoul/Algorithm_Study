import sys
input = sys.stdin.readline
N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def multiple(A, B, N):
    tmp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                tmp[i][j] += A[i][k] * B[k][j]
    for i in range(N):
        for j in range(N):
            tmp[i][j] %= 1000
    return tmp


def solution(arr, B):
    if B == 1:
        for i in range(N):
            for j in range(N):
                arr[i][j] %= 1000
        return arr
    elif B == 2:
        return multiple(arr, arr, N)
    else:
        k = solution(arr, B//2)
        if B % 2 == 0:
            return multiple(k, k, N)
        else:
            return multiple(multiple(k, k, N), arr, N)


for i in solution(arr, B):
    print(*i)
