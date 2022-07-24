def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    map = [[0] * 11 for i in range(50)]
    
    for i in rectangle:
        for j in range(i[1], i[3]+1):
            for k in range(i[0], i[2]+1):
                map[j][k] = 1
    
    # 솔직히 모르겠습니다...
    
    for i in reversed(map):
        print(i)
    
    return answer