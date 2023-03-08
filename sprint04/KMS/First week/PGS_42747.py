def solution(citations):
    answer = 0
    count = []
    for h in range(max(citations)):
        print(h)
        cnt = 0
        cnt1 = 0
        for i in citations:
            if h <= i:
                cnt += 1
            if h >= i:
                cnt1 += 1
        if cnt >= h and cnt1 <= h and answer < h:
            answer = h
    return answer