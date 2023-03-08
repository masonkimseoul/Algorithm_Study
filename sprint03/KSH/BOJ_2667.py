from collections import deque

def bfs(loc, lst):

    queue = deque()
    box = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    cnt = 0

    queue.append(loc)

    while (queue):
        x, y = queue.popleft();
        lst[y][x] = 0
        cnt += 1
        for i in box:
            x_, y_ = i
            if x+x_ >= 0 and x+x_ < len(lst) and y+y_ >= 0 and y+y_ < len(lst):
                if lst[y+y_][x+x_] == 1 and [x+x_, y+y_] not in queue:
                    queue.append([x+x_, y+y_])

    return cnt

if __name__ == "__main__":

    n = int(input())
    lst = []
    for i in range(n):
        lst.append(list(map(int, input())))
    cnt_lst = []

    for i in range(n):
        for j in range(n):
            if lst[i][j] == 1:
                cnt_lst.append(bfs([j, i], lst))
    
    print(len(cnt_lst))
    for i in sorted(cnt_lst):
        print(i)
