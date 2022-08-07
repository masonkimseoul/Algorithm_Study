def solution(N,number):
    N=str(N)
    number=str(number)

    oper = ['*', '+', '-', '//']
    lst=[{N*(i+1)} for i in range(8)]

    for i in range(8):
        for j in range(i):
            for k in lst[j]:
                for l in lst[i-j-1]:
                    for m in oper:
                        if int(l)<1:
                            continue
                        result=eval(k+m+l)
                        if result>32000:
                            continue
                        lst[i].add(str(result))
        if number in lst[i]:
            return i+1
    return -1

print(solution(2,11))