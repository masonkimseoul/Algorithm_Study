def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers = (sorted(numbers, key=lambda x: x * 5, reverse=True))

    for n in numbers:
        answer += str(n)
    return str(int(answer))