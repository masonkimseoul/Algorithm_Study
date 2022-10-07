def solution(brown, yellow):
    answer = []
    gob = brown + yellow
    for x in range(1, gob):
        if gob % x == 0:
            y = gob // x
            if 2*(x+y) == brown + 4:
                answer.append(x)
                answer.append(y)
                break
    
    return sorted(answer, reverse = True)