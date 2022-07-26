def solution(numbers):
    answer=''
    numbers=[str(number) for number in numbers]
    numbers.sort(key=lambda x:x*3, reverse=True)

    for number in numbers:
        answer+=number
    if eval(answer)==0:
        return "0"

    return answer