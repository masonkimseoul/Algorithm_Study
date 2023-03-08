def solution(number, k):
    stack=[]
    for i in number:
        while stack:
            if stack[-1]<i and k>0:
                k-=1
                stack.pop()
            else:
                break
        stack.append(i)
    return ''.join(stack[:len(number)-k])