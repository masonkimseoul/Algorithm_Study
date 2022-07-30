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

    # 함수를 들어갔다가 나오는 게 메모리에 큰 영향을 끼치나..? => 왜 DFS는 터지고 BFS는 괜찮은 걸까?
    # DFS의 경우, 스택이 쌓이기 때문에 메모리 초과가 나온다고 한다.
    # 참고: https://velog.io/@a87380/1926%EB%B2%88-%EA%B7%B8%EB%A6%BC-%ED%8C%8C%EC%9D%B4%EC%8D%AC

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