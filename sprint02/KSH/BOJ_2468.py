import sys

sys.setrecursionlimit(10**7)

def dfs(loc, lst, visited, k):
    x_, y_ = loc
    if not (x_>=0 and x_<len(lst)) or not (y_>=0 and y_<len(lst)):
        return
    if visited[y_][x_] or lst[y_][x_] <= k:
        return

    visited[y_][x_] = 1

    box = [[0,1], [1,0], [0,-1], [-1,0]]
    for i in box:
        x = x_+i[0]
        y = y_+i[1]
        dfs([x, y], lst, visited, k)


if __name__ == "__main__":
    n = int(input())
    lst = []
    cnt_lst = []
    for i in range(n):
        lst.append(list(map(int, input().split())))

    for k in range(max(map(max, lst))):
        visited = [[0]*n for i in range(n)]
        cnt = 0
        for y in range(n):
            for x in range(n):
                if (lst[y][x] > k and not visited[y][x]):
                    dfs([x, y], lst, visited, k)
                    cnt += 1

        cnt_lst.append(cnt)

    print(max(cnt_lst))