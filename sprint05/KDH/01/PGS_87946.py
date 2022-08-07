from itertools import permutations


def solution(k, dungeons):
    answer = -1

    for ways in permutations(dungeons):
        tmp = k
        answer_ = 0
        for d in ways:
            if d[0] <= tmp:
                tmp -= d[1]
                answer_ += 1
                continue
            else:
                break
        if answer_ != 0:
            answer = max(answer, answer_)
        if answer == len(dungeons):
            return answer
    return answer
