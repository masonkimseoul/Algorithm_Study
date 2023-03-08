def solution(scores):
    answer = 1
    prev = 0
    A, B = scores[0]
    scores.sort(key=lambda x: (-x[0], x[1]))
    for i in scores:
        a, b = i
        if a > A and b > B:
            return -1
        if prev <= b:
            if A+B < a+b:
                answer += 1
            prev = b
    return answer
