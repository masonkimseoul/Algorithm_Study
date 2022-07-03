from collections import deque

def bfs(lst):

    queue = deque()

    queue.append([0, 0])

    box = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    while queue:
        x, y = queue.popleft()
        for i in box:
            x_, y_ = i
            a = x + x_
            b = y + y_
            if (a >= 0 and a < len(lst[0])) and (b >= 0 and b < len(lst)):
                if lst[b][a] == 1 and not (a == 0 and b == 0):
                    lst[b][a] = lst[y][x] + 1
                    queue.append([a, b])




if __name__ == "__main__":
    n, m = map(int, input().split())
    lst = []
    for i in range(n):
        lst.append(list(map(int, input())))
    
    bfs(lst)

    print(lst[n-1][m-1])
