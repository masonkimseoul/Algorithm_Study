
if __name__ == "__main__":
    n, m = map(int, input().split())
    map_ = []

    for i in range(n):
        map_.append(list(input()))
    visited = [[0 for i in range(n)] for j in range(n)]
    box = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    def dfs(x, y):

        visited[y][x] = 1

        for i in box:
            x_, y_ = x+i[0], y+i[1]
            if 0<=x_<len(map_[0]) and 0<=y_<len(map_):
                if map_[y_][x_] == '.' and visited[y_][x_] == 0:
                    dfs(x_, y_)

    for y in range(n):
        for x in range(m):
            if x == 0 or x == n - 1 or y == 0 or y == n - 1:
                if map_[y][x] == '.':
                    dfs(x, y)
    
    cnt = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                cnt += 1

    print(n * n - cnt)
