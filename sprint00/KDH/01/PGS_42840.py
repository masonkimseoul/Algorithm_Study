def solution(answers):
    answer = []
    
    people = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    max_ = -1
    for i in range(3):
        cnt = 0
        for j in range(len(answers)):
            if answers[j] == people[i][j % len(people[i])]:
                cnt += 1
        if cnt > max_:
            answer = [i+1]
            max_ = cnt
        elif cnt == max_:
            answer.append(i+1)
    
    return answer
