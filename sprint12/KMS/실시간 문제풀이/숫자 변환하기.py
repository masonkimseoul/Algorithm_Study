from collections import deque


def solution(x, y, n):
    answer = 0

    def BFS(y, x, n):
        q = deque()
        q.append((y, 0))
        while q:
            a, cnt = q.popleft()
            if a == x:
                return cnt
            if a < x:
                continue
            if a < x and a - int(a) > 0:
                return -1
            q.append((a - n, cnt+1))
            q.append((a / 2, cnt+1))
            q.append((a / 3, cnt+1))
        return -1
    answer = BFS(y, x, n)
    return answer


print(solution(10, 40, 5))
