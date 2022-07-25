from collections import deque
import sys

input = sys.stdin.readline

def bfs(graph, id, n):

    queue = deque()
    visited = [-1 for i in range(n+1)]
    visited[id] = 0
    queue.append(id)

    while queue:
        id_ = queue.popleft()

        for i in graph[id_]:
            if visited[i] == -1:
                visited[i] = visited[id_] + 1
                queue.append(i)

    return sum(visited) + 1

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for j in range(n + 1)]
    for i in range(m):
        line = list(map(int, input().split()))
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])
    
    cnt_lst = []

    for i in range(1, n + 1):
        cnt_lst.append(bfs(graph, i, n))

    min_ = min(cnt_lst)
    answer = 0

    for idx, val in enumerate(cnt_lst):
        if val == min_:
            answer = idx
            break

    print(answer + 1)


