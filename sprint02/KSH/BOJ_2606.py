
from collections import deque

# bfs
def bfs(lst):

    queue = deque()
    visited = []
    queue.extend(lst[1])
    while queue:
        l = queue.popleft()
        if l not in visited:
            visited.append(l)
            queue.extend(lst[l])
    
    return (len(visited) - 1)


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    lst = [[] for i in range(n + 1)]
    visited = [0] * (n + 1)

    for i in range(m):
        a, b = map(int, input().split())
        lst[a].append(b)
        lst[b].append(a)
    
    print(bfs(lst))