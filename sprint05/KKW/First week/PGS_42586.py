from collections import deque
def solution(progresses,speeds):
    answer=[]
    cnt=0
    day=1
    progresses=deque(progresses)
    speeds=deque(speeds)
    while len(progresses)>0:
        if progresses[0]+speeds[0]*day>=100:
            progresses.popleft()
            speeds.popleft()
            cnt+=1
        else:
            day+=1
            if cnt>0:
                answer.append(cnt)
                cnt=0
    answer.append(cnt)
    return answer