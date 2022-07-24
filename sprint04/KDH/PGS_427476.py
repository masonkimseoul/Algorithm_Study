def solution(numbers):
    answer = ''

    if sum(numbers) == 0:
        return "0"

    numbers_ = [str(num) for num in numbers]
    numbers__ = sorted(numbers_, key=lambda x: x*3, reverse=True)
    answer = ''.join(numbers__)

    return answer
