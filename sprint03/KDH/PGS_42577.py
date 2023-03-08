# 0.
# def solution(phone_book):
#     answer = True
#     arranged = sorted(phone_book)
#     for i in range(len(arranged)-1):
#         length = len(arranged[i])
#         if arranged[i] == arranged[i+1][:length]:
#             answer = False
#             break
#     return answer

# 1. hash
def solution(phone_book):
    answer = True
    hash_table = {}
    for num in phone_book:
        hash_table[hash(num)] = 1

    for num in (phone_book):
        tmp = ""
        for j in (num):
            tmp += j
            if tmp != num and hash(tmp) in hash_table.keys():
                return False
    return answer
