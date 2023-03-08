import math


def solution(progresses, speeds):
    answer = []
    for p, s in zip(progresses, speeds):
        if not answer or release < math.ceil((100-p)/s):
            release = math.ceil((100-p)/s)
            answer.append(1)
        else:
            answer[-1] += 1

    return answer
