def solution(number, k):
    answer = ''
    stack = []
    for i in number:
        while stack and i > stack[-1]:
            if k > 0:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(i)
    while k > 0:
        stack.pop()
        k -= 1
    answer = answer.join(stack)
    return answer