def middle_func(num, idx):
    sum = 0
    
    for i in range(idx):
        sum += num * (5**i)
    
    return sum

def solution(word):
    answer = 0
    
    dic = {"A":1, "E":2, "I":3, "O":4, "U":5}
    
    for idx, i in enumerate(word):
        answer += middle_func(dic[i]-1, 5-idx)
        # print(f"num: {dic[i]-1}, idx: {5-idx}, sum:{middle_func(dic[i]-1, 5-idx)}")
    
    answer += len(word)
    
    return answer