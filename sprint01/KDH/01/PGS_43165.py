from itertools import product

def solution(numbers, target):
    answer = 0
    numbers_ = [(x, -x) for x in numbers]
    sums = list(map(sum, list(product(*numbers_))))
    return sums.count(target)