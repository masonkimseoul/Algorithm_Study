from itertools import permutations

def check_decimal(num):
    count = 0
    for i in range(1, num + 1):
        if (num % i == 0):
            count += 1
        if count > 2:
            return False
    if count == 2:
        return True
    return False

def solution(numbers):
    answer = 0
    
    lst = list(numbers)
    llst = []
    
    # 지금 막히고 있는 부분이, 어떻게 숫자들을 조합해서 케이스들을 만들 것인지...
    # => A. 내가 잘 모르는 파이썬의 문법이 있었다.
    # => 순열 (permutations)
    
    for i in range(len(lst)):
        l = list(set(list(map(''.join, permutations(lst, i + 1)))))
        llst.extend(list(map(int, l)))
    
    # map함수에 대한 명확한 정리가 필요함.
    
    for i in list(set(llst)):
        if (check_decimal(i)):
            answer += 1
    
    return answer