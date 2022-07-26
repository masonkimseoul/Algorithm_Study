# 효율성 0점 풀이

# def check(lst, k):
#     for i in lst:
#         if i < k:
#             return False
#     return True

# def solution(scoville, K):
#     answer = -1
#     lst = []
#     for i in scoville:
#         if i >= K:
#     cnt = 0
#     while True:
#         if check(scoville, K):
#             answer = cnt
#             break
#         if len(scoville) < 2:
#             break
#         cnt += 1
#         scoville.sort(reverse = True)
#         a = scoville.pop()
#         b = scoville.pop()
#         scoville.append(a + 2*b)

#     return answer

# ------------- 효율성 통과 코드 (Heap으로 구현)--------------

import heapq

def solution(scoville, K):
    answer = -1
    
    cnt = 0
    heapq.heapify(scoville)

    while scoville[0] < K and len(scoville) > 1:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + 2*b)
        cnt += 1
    
    if scoville[0] >= K:
        answer = cnt
    
    return answer