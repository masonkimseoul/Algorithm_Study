
def solution(numbers):
    answer = ''
    
    answer_lst = []
    lst = list(map(str, numbers))
    lst.sort(key = lambda x : (x*3), reverse = True)
        
    answer = str(int("".join(lst)))
        
    return answer