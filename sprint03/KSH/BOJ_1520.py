import sys

sys.setrecursionlimit(10**7)

def dfs(x, y, lst, visited):

    box = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    if (x == len(lst[0])-1 and y == len(lst)-1):
        return 1

    if (visited[y][x] != -1):
        return visited[y][x]

    total = 0
    for i in box:
        x_, y_ = x+i[0], y+i[1]
        if 0<=x_<len(lst[0]) and 0<=y_<len(lst):
            if (lst[y][x] > lst[y_][x_]):
                total += dfs(x_, y_, lst, visited)
    
    visited[y][x] = total
    return total


if __name__ == "__main__":
    n, m = map(int, input().split())
    lst = []
    for i in range(n):
        lst.append(list(map(int, input().split())))
    visited = [[-1 for i in range(len(lst[0]))] for j in range(len(lst))]
    
    print(dfs(0, 0, lst, visited))
