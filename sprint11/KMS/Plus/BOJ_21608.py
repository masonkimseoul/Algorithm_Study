
def find_seat(L):
    A, a1, a2, a3, a4 = L
    tmp_seats = []
    # 좋아 하는 친구 수 찾기
    for i in blank:
        x, y = i
        like = 0
        blank_num = 0
        nx = [1, -1, 0, 0]
        ny = [0, 0, 1, -1]
        for k in range(4):
            dx = nx[k] + x
            dy = ny[k] + y
            if 0 <= dx < n and 0 <= dy < n:
                if graph[dx][dy] == a1 or graph[dx][dy] == a2 or graph[dx][dy] == a3 or graph[dx][dy] == a4:
                    like += 1
                if graph[dx][dy] == 0:
                    blank_num += 1
        tmp_seats.append((like, blank_num, x, y))
    tmp_seats.sort(key=lambda x: [-x[0], -x[1], x[2], x[3]])
    x = tmp_seats[0][2]
    y = tmp_seats[0][3]
    graph[x][y] = A
    index = -1
    for idx, data in enumerate(blank):
        x1, y1 = data
        if x1 == x and y1 == y:
            index = idx
            break
    blank.pop(index)


def find_like(graph, L):
    result = 0
    L.sort()
    for i in range(n):
        for j in range(n):
            cnt = 0
            index = graph[i][j]-1
            A, a1, a2, a3, a4 = L[index]
            nx = [1, -1, 0, 0]
            ny = [0, 0, 1, -1]
            for k in range(4):
                dx = nx[k] + i
                dy = ny[k] + j
                if 0 <= dx < n and 0 <= dy < n:
                    if graph[dx][dy] == a1 or graph[dx][dy] == a2 or graph[dx][dy] == a3 or graph[dx][dy] == a4:
                        if cnt == 0:
                            cnt = 1
                        else:
                            cnt *= 10
            result += cnt
    return result


n = int(input())
L = [list(map(int, input().split())) for _ in range(n*n)]
graph = [[0 for _ in range(n)] for _ in range(n)]
blank = []
for i in range(n):
    for j in range(n):
        blank.append((i, j))

for i in L:
    find_seat(i)
print(find_like(graph, L))
