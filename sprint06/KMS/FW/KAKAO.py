def solution(p):
    answer = ''
    # 1. 빈 문자열인 경우 반환
    if p == '':
        return answer
    else:
        open_count = 0
        close_count = 0
        u = []
        v = list(p)
        tmp = v.pop(0)
        if tmp == '(':
            open_count +=1
        else:
            close_count +=1
        u.append(tmp)
        while open_count != close_count:
            tmp = v.pop(0)
            if tmp == '(':
                open_count +=1
            else:
                close_count +=1
            u.append(tmp)
        flag = 0
        stack =[]
        for i in u:
            if not stack:
                if i == ')':
                    flag = 1
                    break
                stack.append(i)
            else:
                if i == '(':
                    stack.append(i)
                else:
                    stack.pop()
        if stack:
            flag = 1
        stru = ''.join(u)
        strv = ''.join(v)
        if flag == 0:
            answer = stru + solution(strv)
            return answer
        else:
            blank = '(' + solution(strv) + ')'
            u.pop(0)
            u.pop()
            reverseu =''
            for i in u:
                if i == '(':
                    reverseu += ')'
                else:
                    reverseu += '('
            blank += reverseu
            return blank