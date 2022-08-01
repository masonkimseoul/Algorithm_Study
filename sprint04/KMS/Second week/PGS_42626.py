mport heapq

def solution(scovile, K):
    heapq.heapify(scovile)
    cnt = 0
    while len(scovile)>1 : 
        heapq.heappush(scovile, heapq.heappop(scovile) +(heapq.heappop(scovile)*2))
        cnt +=1
        
        if scovile[0] >= K:
            return cnt
    return -1