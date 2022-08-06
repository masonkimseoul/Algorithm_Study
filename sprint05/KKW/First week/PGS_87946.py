from itertools import permutations

def solution(k, dungeons):
    answer=0
    for i in permutations(dungeons):
        fatigability=k
        tmp=0
        for j in i:
            if j[0]<=fatigability:
                fatigability-=j[1]
                tmp+=1
            else:
                break

        answer=max(answer,tmp)
        if answer==len(dungeons):
            return answer
    return answer