from collections import deque

def compare(word1, word2):
    cnt = 0
    for idx, word in enumerate(word1):
        if word2[idx] == word:
            cnt += 1
    if cnt >= len(word1) - 1:
        return True
    return False

def bfs(target, word, lst, visited):
    queue = deque()
    queue.append(word)
    cnt = 0
    tmp_lst = []
    
    while queue:
        w = queue.popleft()
        if w == target:
            return cnt
        for i in lst:
            if not visited[i] and compare(w, i):
                visited[i] = 1
                tmp_lst.append(i)
                # queue.append(i)
        if not queue:
            queue.extend(tmp_lst)
            tmp_lst = []
            cnt += 1
        
    return False


def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    visited = dict()
    for i in words:
        visited[i] = 0
    
    result = bfs(target, begin, words, visited)
    
    if result == False:
        answer = 0
    else:
        answer = result
    
    return answer

# test case 공유
# 링크: https://programmers.co.kr/questions/15939

# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
# print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"]), 1)
# print(solution("1234567000", "1234567899", [
#       "1234567800", "1234567890", "1234567899"]), 3)
# print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"]), 4)
