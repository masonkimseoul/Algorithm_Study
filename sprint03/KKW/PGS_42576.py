def solution(participant, completion):
    dic={}
    answer=''
    idx=0

    for i in participant:
        dic[hash(i)]=i
        idx+=int(hash(i))

    for j in completion:
        idx-=hash(j)

    answer=dic[idx]
    return answer