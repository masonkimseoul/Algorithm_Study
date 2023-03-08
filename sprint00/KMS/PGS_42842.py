def solution(brown, yellow):
    answer = []
    S = brown + yellow
    for i in range(1,max(brown,yellow)):
        a = i
        b = S / a
        if((a-2) * (b-2) == yellow):
            break
    if(a <= b):
        answer.append(b)
    answer.append(a)
    return answer