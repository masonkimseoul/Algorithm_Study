from collections import deque
def solution(progresses, speeds):
    answer = []
    complete = deque()
    for i in range(len(progresses)):
        cnt = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            cnt +=1
        complete.append(cnt)
    
    cnt = 0
    while complete:
        tmp = complete[0]
        while complete:
            if complete[0] <= tmp:
                complete.popleft()
                cnt +=1
            else:
                break
        if cnt != 0:
            answer.append(cnt)
            cnt = 0
    return answer


