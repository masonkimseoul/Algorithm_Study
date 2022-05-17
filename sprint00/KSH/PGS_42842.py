def solution(brown, yellow):
    answer = []
    
    total = brown + yellow
    case = []
    
    for i in range(1, total):
        if total % i == 0:
            case.append([i, (total // i)])
    
    # print(case)
    
    for i in case:
        if (2 * i[0] + 2 * (i[1] - 2) == brown and i[0] >= i[1]):
            answer.extend(i)
            break    

    return answer