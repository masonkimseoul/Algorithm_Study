from collections import deque


def checkDiff(word1, word2):
    cnt = 0

    for i, j in zip(word1, word2):
        if i != j:
            cnt += 1
    return cnt


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer

    visited = [False] * len(words)

    queue = deque()
    queue.append([begin, 0])
    while queue:
        x, cnt = queue.popleft()
        if x == target:
            return cnt
        for i in range(len(words)):
            if checkDiff(x, words[i]) == 1 and not visited[i]:
                queue.append([words[i], cnt+1])
                visited[i] = True

    return answer
