from collections import deque

def dfs(idx, dic, visited):
    for i in dic[idx]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic, visited)

def bfs(k, dic):
    queue = deque()
    visited = [k]
    queue.append(k)
    
    while queue:
        l = queue.popleft()
        for i in dic[l]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    return visited


if __name__ == "__main__":

    n, m, k = map(int, input().split())
    
    dic = dict()
    for i in range(n):
        dic[i + 1] = []

    for i in range(m):
        a, b = map(int, input().split())
        dic[a].append(b)
        dic[b].append(a)
    
    for i in range(n):
        dic[i + 1].sort()

    visited_dfs = [k]
    dfs(k, dic, visited_dfs)
    visited_bfs = bfs(k, dic)
    
    print(*visited_dfs)
    print(*visited_bfs)

