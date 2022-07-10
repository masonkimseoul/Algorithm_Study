def solution(genres, plays):
    answer = []
    
    dic = dict()
    
    for idx, val in enumerate(genres):
        if dic.get(val) == None:
            dic[val] = [[idx, plays[idx]]]
        else:
            dic[val].append([idx, plays[idx]])
    
    # dic = sorted(dic, key = lambda value:sum([i[1] for i in value[1]]), reverse = True)
    
    dic = dict(sorted(dic.items(), key = lambda value:sum([i[1] for i in value[1]]), reverse = True))
    
    for k in dic.keys():
        dic[k] = sorted(dic[k], key = lambda lst:lst[1], reverse = True)
        num = len(dic[k])
        if num > 2:
            num = 2
        for j in range(num):
            answer.append(dic[k][j][0])
    
    # print(dic)
    
    return answer