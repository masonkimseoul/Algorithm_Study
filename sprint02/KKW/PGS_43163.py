from collections import deque
def solution(begin, target, words):
    answer = 0
    d = deque()
    d.append([begin, 0])
    visited = [0 for _ in range(len(words))]
    while d:
        start, cnt = d.popleft()
        if start == target:
            answer = cnt
            break
        for i in range(len(words)):
            tmpcnt = 0
            if not visited[i]:
                for j in range(len(start)):
                    if start[j] != words[i][j]: tmpcnt += 1
                if tmpcnt == 1:
                    d.append([words[i], cnt + 1])
                    visited[i] = 1

    return answer