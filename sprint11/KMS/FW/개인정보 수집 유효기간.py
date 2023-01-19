def solution(today, terms, privacies):
    year, month, day = today.split('.')
    answer = []
    for idx, i in enumerate(privacies):
        date, name = i.split()
        pyear, pmonth, pday = date.split('.')
        result = 0
        # 일로 변환 해서
        Y = int(pyear) - int(year)

        M = int(month) - int(pmonth)

        D = int(day) - int(pday)

        result += -(Y * 12)
        result += M
        if D < 0:
            result -= 1
        for j in terms:
            N, term = j.split()
            if N == name:
                if int(term) <= result:
                    answer.append(idx+1)
    return answer
