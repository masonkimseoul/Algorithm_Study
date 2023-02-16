from collections import deque
L = list(map(str, input().strip()))
D = {'+': 0, '-': 0, '*': 1, '/': 1}
stack = []
for i in L:
    if 'A' <= i <= 'Z':
        print(i, end='')
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                print(stack.pop(), end='')
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                print(stack.pop(), end='')
            stack.pop()
        else:
            while stack and stack[-1] != '(':
                print(stack.pop(), end='')
            stack.append(i)
while stack:
    print(stack.pop(), end='')
