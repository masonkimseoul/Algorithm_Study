import sys
from sys import stdin
from collections import deque
import copy

chess = deque(list(input().rstrip()) for _ in range(8))

move = [[0, 0],
        [0, -1],
        [0, 1],
        [-1, 0],
        [1, 0],
        [-1, -1],
        [1, -1],
        [1, 1],
        [-1, 1]]


def bfs(chess):
    q = deque()
    q.append((7, 0, chess, 0))
    while q:
        x, y, C, cnt = q.popleft()
        if C[x][y] == '#':
            continue
        if x == 0 and y == 7:
            return 1
        if cnt >= 7:
            return 1
        for i in range(9):
            next_x = x + move[i][0]
            next_y = y + move[i][1]
            if next_x < 0 or next_x >= 8 or next_y < 0 or next_y >= 8:
                continue
            if C[next_x][next_y] == '#':
                continue
            T = copy.deepcopy(C)
            T.pop()
            T.appendleft(['.' for _ in range(8)])
            q.append((next_x, next_y, T, cnt+1))
    return 0


print(bfs(chess))
