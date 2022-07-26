import sys
from collections import deque

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    lst = []

    for i in range(n):
        lst.append(list(map(int, input().split())))
    
    visited = [[0 for i in range(len(lst[0]))] for j in range(len(lst))]
    box = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    # dfs는 메모리 초과 뜸... ㅆㅂ
    def dfs(x, y):
        global cnt

        lst[y][x] = 0
        cnt += 1
        for i in box:
            x_, y_ = x+i[0], y+i[1]
            if 0<=x_<len(lst[0]) and 0<=y_<len(lst):
                if lst[y_][x_] == 1:
                    dfs(x_, y_)

    # --------bfs로 품-------------

    def bfs(x, y):
        queue = deque()
        queue.append([x, y])
        cnt = 0
        lst[y][x] = 0

        while (queue):
            x, y = queue.popleft()
            cnt += 1
            for i in box:
                x_, y_ = x+i[0], y+i[1]
                if 0<=x_<len(lst[0]) and 0<=y_<len(lst):
                    if lst[y_][x_] == 1:
                        lst[y_][x_] = 0
                        queue.append([x_, y_])
        
        return cnt

    cnt_lst = []

    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == 1:
                cnt_lst.append(bfs(j, i))

    print(len(cnt_lst))
    
    if (len(cnt_lst) == 0):
        print(0)
    else:
        print(max(cnt_lst))