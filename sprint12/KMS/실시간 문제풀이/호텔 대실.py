def solution(book_time):
    answer = 0
    a = [0 for i in range(24 * 60 + 10)]
    for i in book_time:
        startH, startM = map(int, i[0].split(':'))
        endH, endM = map(int, i[1].split(':'))
        start = startH * 60 + startM
        end = endH * 60 + endM + 10
        for i in range(start, end):
            a[i] += 1
    answer = max(a)
    return answer
