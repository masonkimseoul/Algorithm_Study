from collections import defaultdict

def solution(genre, play):
    answer=[]
    dic=defaultdict(dict)
    N=len(genre)

    for i, g in genre:
        dic[g][i]=play[i]

    dic=dict(sorted(dic.items(), key=lambda x:(-sum(x[1].values()))))
    for j, k in dic.items():
        dic[j]=dict(sorted(k.items(), key=lambda x:-x[1]))

    for k in dic.values():
        for i,j in enumerate(k.keys()):
            answer.append(j)
            if i==1:
                break

    return answer