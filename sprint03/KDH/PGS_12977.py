# 소수 만들기
from itertools import combinations


def solution(nums):
    list_ = list(combinations(nums, 3))

    def is_decimal(num):
        cnt = 0
        for i in range(1, num):
            if num % i == 0:
                cnt += 1

        if cnt == 1:
            return True
        else:
            return False

    answer = 0

    for a, b, c in (list_):
        if is_decimal(a+b+c):
            answer += 1

    return answer
