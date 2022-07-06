def solution(phone_book):
    answer = True
    
    # 정렬
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
            # 접두사 비교 반복문
                if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
                    return False
                
                
    
    return answer