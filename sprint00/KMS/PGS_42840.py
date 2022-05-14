def solution(answers):
    cnt1 =0
    std1 = [1,2,3,4,5]
    std2 = [2,1,2,3,2,4,2,5]
    std3 = [3,3,1,1,2,2,4,4,5,5]
    cnt = [0, 0, 0]
    for i in answers:
        #case 1
        if(i == std1[cnt1 % 5]):
            cnt[0] = cnt[0] + 1
        # case 2
        if(i == std2[cnt1 % 8]):
            cnt[1] = cnt[1] + 1
        # case 3
        if(i == std3[cnt1 % 10]):
            cnt[2] = cnt[2] + 1
        cnt1 = cnt1 + 1

    result = max(cnt)


    answer = []
    if(result == cnt[0]):
        answer.append(1)
    if(result == cnt[1]):
        answer.append(2)
    if(result == cnt[2]):
        answer.append(3)
    return answer