from collections import deque

def solution(prices):
    answer=[]
    prices=deque(prices)

    while prices:
        cnt=0
        tmp=prices.popleft()
        for i in prices:
            cnt+=1
            if i<tmp:
                break
        answer.append(cnt)
    return answer

prices=[1, 2, 3, 2, 3]
print(solution(prices))