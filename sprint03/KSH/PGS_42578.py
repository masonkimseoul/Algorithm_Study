def solution(clothes):
    answer = 1
    
    a = dict()
    num_lst = []
    
    for i in clothes:
        if a.get(i[1]) == None:
            a[i[1]] = 1
        else:
            a[i[1]] += 1
        
    for i in a:
        answer *= (a[i] + 1)
        
    return answer - 1

# 조합을 이용해서는... 푸는게 아니다.
# 이건 그냥 수학 문제 => 확률과 통계를 공부했는가?