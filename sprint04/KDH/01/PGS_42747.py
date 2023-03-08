def solution(citations):
    answer = 0
    max_ = max(citations)

    for h in range(max_+1):
        cnt = 0
        for c in citations:
            if c >= h:
                cnt += 1
        if cnt >= h:
            answer = h

    return answer
