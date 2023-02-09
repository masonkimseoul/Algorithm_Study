
def solution(maps):
    global R
    answer = []
    row = len(maps[0])
    col = len(maps)
    visit = [[True for _ in range(row)] for _ in range(col)]
    R = []

    def DFS(x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]
        R.append(maps[x, y])
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < col and 0 <= ny < row:
                if visit[nx][ny] and maps[nx][ny] != 'X':
                    visit[nx][ny] = False
                    DFS(nx, ny)

    for idx in range(col):
        for jdx in range(row):
            if maps[idx][jdx] != 'X' and visit[idx][jdx]:
                visit[idx][jdx] = False
                DFS(idx, jdx)
                print(R)

    if answer == []:
        answer.append(-1)
    return answer


solution(["X591X", "X1X5X", "X231X", "1XXX1"])
