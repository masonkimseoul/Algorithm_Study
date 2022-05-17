def solution(answers):
    answer = []

    st1 = [1, 2, 3, 4, 5]
    st2 = [2, 1, 2, 3, 2, 4, 2, 5]
    st3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    stCheck = [0, 0, 0]
    cnt = 0

    for i in answers:
        if (i == st1[cnt % 5]): stCheck[0] = stCheck[0] + 1
        if (i == st2[cnt % 8]): stCheck[1] = stCheck[1] + 1
        if (i == st3[cnt % 10]): stCheck[2] = stCheck[2] + 1
        cnt = cnt + 1

    for i in range(3):
        if (max(stCheck) == stCheck[i]): answer.append(i + 1)

    return answer