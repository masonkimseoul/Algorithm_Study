import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

# 모두 같으면 True 아니면 False


def AllSame(x, y, size):
    prev = graph[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if prev != graph[i][j]:
                return False
            else:
                prev = graph[i][j]
    return True


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = {-1: 0, 0: 0, 1: 0}


def solution(x, y, size):
    if size == 1:
        answer[graph[x][y]] += 1
        return
    if AllSame(x, y, size):
        answer[graph[x][y]] += 1
    else:
        size = size // 3
        for i in range(3):
            for j in range(3):
                solution(x + i * size, y + j*size, size)


solution(0, 0, n)
for i in answer:
    print(answer[i])
