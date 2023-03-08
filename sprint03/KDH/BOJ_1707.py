import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def dfs(x, f):
    visited[x] = f
    for v in graph[x]:
        if visited[v] == 0:
            if not dfs(v, -f):
                return False
        elif visited[v] == visited[x]:
            return False
    return True


for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    res = True
    for i in range(1, V+1):
        if visited[i] == 0:
            res = dfs(i, 1)
            if not res:
                break
    print("YES" if res else "NO")
