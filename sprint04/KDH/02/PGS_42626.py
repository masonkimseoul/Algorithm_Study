import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >= 2:
        if scoville[0] >= K:
            return answer
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)

        heapq.heappush(scoville, min1+2*min2)
        answer += 1

    return answer if scoville[0] >= K else -1
