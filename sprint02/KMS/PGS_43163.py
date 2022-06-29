import copy
answer = 99
def check(word_a, word_b):
    cnt = 0
    for i in range(len(word_a)):
        if(word_a[i] == word_b[i]):
            cnt = cnt +1;
    if(cnt == len(word_a)-1):
        return 1
    else:
        return 0
    
def dfs(begin, target, words, count):
    global answer
    count += 1
    if words == []:
        return;
    for nextword in words:
        if check (begin,nextword):
            if nextword == target:
                answer = min(answer, count)
                return
            nextwords = words.copy()
            nextwords.remove(nextword)
            dfs(nextword, target, nextwords, count)
            
    
def solution(begin, target, words):
    global answer
    words.sort()
    print(words)
    dfs(begin, target, words, 0)
    
    if(answer > 50):
        return 0
    return answer