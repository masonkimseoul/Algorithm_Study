def solution(number, k):
    answer = ''
        
    stack = [number[0]]
    
    for i in number[1:]:
        while (len(stack) > 0 and k > 0 and stack[-1] < i):
            stack.pop()
            k -= 1
        stack.append(i)

    for i in range(k):
        stack.pop()
        
    answer = "".join(stack)
    
    return answer