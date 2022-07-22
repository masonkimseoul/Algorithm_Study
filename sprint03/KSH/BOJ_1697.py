from collections import deque

def bfs(n, m):
    queue = deque()
    visited = [0 for i in range(100001)]
    queue.append(n)
    visited[n] = 0
    while queue:
        val = queue.popleft()
        if (val == m):
            return visited[val]
        if (0<=val-1<len(visited)) and visited[val - 1] == 0:
            queue.append(val - 1)
            visited[val - 1] = visited[val] + 1
        if (0<=val+1<len(visited)) and visited[val + 1] == 0:
            queue.append(val + 1)
            visited[val + 1] = visited[val] + 1
        if (0<=2*val<len(visited)) and visited[2*val] == 0:
            queue.append(2*val)
            visited[2*val] = visited[val] + 1

if __name__ == "__main__":
    n, m = map(int, input().split())

    print(bfs(n, m))

