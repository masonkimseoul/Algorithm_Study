def solution(info, query):
    answer = []
    language = {}
    major = {}
    carrer = {}
    food = {}
    score = {}
    info_table = {}
    index_list = []
    index = 1
    for i in info:
        L = i.split(' ')
        if L[0] not in language.keys():
            language[L[0]] = []
        language[L[0]].append(index)
        if L[1] not in major.keys():
            major[L[1]] = []
        major[L[1]].append(index)
        if L[2] not in carrer.keys():
            carrer[L[2]] = []
        carrer[L[2]].append(index)
        if L[3] not in food.keys():
            food[L[3]] = []
        food[L[3]].append(index)
        score[index] = L[4]
        index_list.append(index)
        index+=1
    query_table = []
    
    
    for i in query:
        L = i.split(' ')
        while 'and' in L:
            L.remove('and')
        cnt = 0
        c = set(index_list)
        if not L[0] == '-':
            c = c & set(language[L[0]])
        if not L[1] == '-':
            c = c & set(major[L[1]])
        if not L[2] == '-':
            c = c & set(carrer[L[2]])
        if not L[3] == '-':
            c = c & set(food[L[3]])
        c5 = min(c5)
        
        for j in c5:
            if int(score[j]) >= int(L[4]):
                cnt+=1
        answer.append(cnt)

    return answer
print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))