import itertools

def is_prime_number(x):
    if(x<=1):
        return False
    for i in range(2, x):
        if x % i == 0:
            return False 
    return True


def solution(numbers):
    answer = 0
    list1 = []
    
    for i in range(0,len(numbers)):
        nPr = itertools.permutations(numbers, i+1)
        nPr = list(nPr)
        for j in nPr:
            # print('j = ',j)
            result =''
            result = result.join(j)
            list1.append(int(result))
    my_list = []
    for v in list1:
        if v not in my_list:
            my_list.append(v)
        
    for v in my_list:
        if(is_prime_number(v) == True):
            answer = answer+1
            print(v)
    print(answer)
    return answer