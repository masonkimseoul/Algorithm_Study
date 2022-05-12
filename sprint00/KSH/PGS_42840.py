def solution(answers):
    
    answer = []
    
    num = len(answers)
    
    supo_1 = []
    supo_2 = []
    supo_3 = []
    repo = [0, 0, 0]
    
    for i in range(num):
        supo_1.append((i % 5) + 1)

    for i in range((num // 8) + 1):
        supo_2.extend([2, 1, 2, 3, 2, 4, 2, 5]);
    
    for i in range((num // 10) + 1):
        supo_3.extend([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])

        
    for i in range(num):
        if supo_1[i] == answers[i]:
            repo[0] += 1
        if supo_2[i] == answers[i]:
            repo[1] += 1
        if supo_3[i] == answers[i]:
            repo[2] += 1
        else:
            pass
        
    n = max(repo)
    
    for i in range(3):
        if repo[i] == n:
            answer.append(i+1)
            
    return answer