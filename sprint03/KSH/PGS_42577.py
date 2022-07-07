def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    for idx, value in enumerate(phone_book):
        if idx == len(phone_book) - 1:
            break
        if value == phone_book[idx+1][0:len(value)]:
            return False
    return True
    
