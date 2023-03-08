def solution(participant, completion):
    answer = ''
    dic = dict()
    for i in participant:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    
    for i in completion:
        dic[i] -= 1
    
    for i in dic:
        if dic[i] == 1:
            answer = i
            break
    
    return answer