def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in arr[1:]:
        tmp = answer.pop()
        if tmp == i:
            answer.append(tmp)
            continue
        else:
            answer.append(tmp)
            answer.append(i)
        
        
    return answer