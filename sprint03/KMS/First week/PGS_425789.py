def solution(genres, plays):
    answer = []
    a = dict()
    b = dict()
    c = list()
    MAX =0
    for i in range(len(genres)):
        if genres[i] in a.keys():
            a[genres[i]].append((plays[i],i))
        else:
            a[genres[i]] = []
            a[genres[i]].append((plays[i],i))
            
    sort = dict()        
            
    
    for i in a.keys():
        sum = 0
        for j in a[i]:
            sum += j[0]
        sort[i]=sum
    
    sort = sorted(sort.items(), key = lambda item : -item[1]) 
    for i in sort:
        
        a[i[0]].sort(key=lambda x:-x[0])
        cnt = 0
        for i in a[i[0]]:
            if(cnt >= 2):
                break
            answer.append(i[1])
            cnt += 1
        
    return answer