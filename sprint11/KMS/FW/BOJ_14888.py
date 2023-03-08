import itertools
n = int(input())
L = list(map(int, input().split()))

# 0 -> +
# 1 -> -
# 2 -> *
# 3 -> /

sign_num = list(map(int, input().split()))
# 연산자 리스트 구하기
sign_list = []
for idx, sign in enumerate(sign_num):
    if idx == 0:
        for i in range(sign):
            sign_list.append('+')
    elif idx == 1:
        for i in range(sign):
            sign_list.append('-')
    elif idx == 2:
        for i in range(sign):
            sign_list.append('*')
    else:
        for i in range(sign):
            sign_list.append('/')
# 연산자 조합 만들기

T = list(itertools.permutations(sign_list, n-1))
# print(T)
R = []
for i in T:
    TT = L[:]
    result = TT.pop(0)
    # print("초기값 : ", result)
    for sign in i:
        tmp = TT.pop(0)
        if sign == '+':
            # print(1)
            result += tmp
        elif sign == '-':
            # print(2)
            result -= tmp
        elif sign == '*':
            # print(3)
            result *= tmp
        else:
            # print(4)
            if result < 0:
                result *= -1
                result //= tmp
                result *= -1
            else:
                result //= tmp
        # print("중간 값 ", result)
    R.append(result)
R.sort()
print(R[-1])
print(R[0])
