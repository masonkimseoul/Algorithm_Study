import sys

input = sys.stdin.readline


# 아  이건 dfs로 풀어야 할 거 같은데?

if __name__ == "__main__":
    r, c = map(int, input().split())
    lst = []

    for i in range(r):
        lst.append(list(map(str, input().rstrip())))

    box = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    check = [0 for i in range(ord('Z') - ord('A') + 1)]
    max_ = 0
    check[ord(lst[0][0]) - 65] = 1

    def dfs(loc, cnt):
        global max_

        max_ = max(cnt, max_)
        x, y = loc
        for i in box:
            x_, y_ = x+i[0], y+i[1]
            if 0<=x_<len(lst[0]) and 0<=y_<len(lst):
                if check[ord(lst[y_][x_]) - ord('A')] == 0:
                    cnt_ = cnt + 1
                    check[ord(lst[y_][x_]) - ord('A')] = 1
                    dfs([x_, y_], cnt_)
                    check[ord(lst[y_][x_]) - ord('A')] = 0
    
    dfs([0, 0], 1)

    print(max_)

# 아래 코드는 시간초과 뜸.

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    r, c = map(int, input().split())
    lst = []

    for i in range(r):
        lst.append(list(map(str, input().rstrip())))

    box = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    check = set()

    dic = dict()
    max_ = 0
    dic[lst[0][0]] = 1

    def dfs(loc, cnt):
        global max_

        max_ = max(max_, cnt)
        x, y = loc        
        for i in box:
            x_, y_ = x+i[0], y+i[1]
            if 0<=x_<len(lst[0]) and 0<=y_<len(lst):
                if dic.get(lst[y_][x_]) == None:
                    dic[lst[y_][x_]] = 1
                    cnt_ = cnt + 1
                    dfs([x_, y_], cnt_)
                    del dic[lst[y_][x_]]
    
    dfs([0, 0], 1)

    print(max_)