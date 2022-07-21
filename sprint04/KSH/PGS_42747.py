def solution(citations):
    answer = 0
    
    for i in range(1, len(citations)+1):
        count = 0
        for val in citations:
            if val >= i:
                count += 1
        if count >= i:
            answer = i
    
    return answer