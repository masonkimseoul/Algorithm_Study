def solution(phone_book):
    answer = True
    
    phone_dict = {}
    for key in phone_book:
        phone_dict[key] = 1
    
    for phone_num in phone_dict:
        tmp = ''
        for num in phone_num:
            tmp += num
            if tmp in phone_dict and tmp != phone_num:
                answer = False
                return answer
    
    return answer

