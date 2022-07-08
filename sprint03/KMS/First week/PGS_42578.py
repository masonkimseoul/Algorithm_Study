from collections import defaultdict

def solution(clothes):
    answer = 1
    aaa = defaultdict(list)
    for i in clothes:
        aaa[i[1]].append(i[0])
    
    a = len(aaa)
    for i in aaa:
        answer *= len(aaa[i]) + 1
    answer -=1

    return answer