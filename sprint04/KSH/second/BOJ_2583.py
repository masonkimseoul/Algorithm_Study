import sys

sys.setrecursionlimit(10**7)

if __name__ == "__main__":
    m, n, k = map(int, input().split())

    map_ = [[0 for i in range(n)] for j in range(m)]
    visited = [[0 for i in range(n)] for j in range(m)]
    box = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    for i in range(k):
        line = list(map(int, input().split()))
        for j in range(line[1], line[3]):
            for z in range(line[0], line[2]):
                map_[j][z] = 1

    def dfs(x, y):

        global cnt
        visited[y][x] = 1
        cnt += 1

        for i in box:
            x_, y_ = x+i[0], y+i[1]
            if 0<=x_<len(map_[0]) and 0<=y_<len(map_):
                if map_[y_][x_] == 0 and visited[y_][x_] == 0:
                    dfs(x_, y_)

    cnt_lst = []

    # for i in map_:
    #     print(i)

    for i in range(len(map_)):
        for j in range(len(map_[0])):
            if map_[i][j] == 0 and visited[i][j] == 0:
                cnt = 0
                dfs(j, i)
                cnt_lst.append(cnt)
    
    print(len(cnt_lst))
    print(*(sorted(cnt_lst)))
