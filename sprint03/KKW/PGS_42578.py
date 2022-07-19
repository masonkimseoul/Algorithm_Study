def solution(clothes):
    answer={}
    for i, j in clothes:
        if j not in answer:
            answer[j]=2
        else:
            answer[j]+=1

    cnt=1
    for i in answer.values():
        cnt*=i

    return cnt-1