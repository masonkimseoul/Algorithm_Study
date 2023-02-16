def solution(s, skip, index):
    answer = ''
    for i in s:
        cnt = 0
        t = ord(i)
        last = index
        while cnt != last:
            cnt += 1
            t += 1
            if t == ord('z') + 1:
                t = ord('a')
            if chr(t) in skip:
                last += 1
        answer += chr(t)
    return answer
