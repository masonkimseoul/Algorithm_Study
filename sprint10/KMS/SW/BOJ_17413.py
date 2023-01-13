
S = input()
size = len(S)
stack = []
i = 0
while (i < size):
    if S[i] == '<':
        while stack:
            print(stack.pop(), end='')
        while (True):
            if S[i] == '>':
                print(S[i], end='')
                break
            print(S[i], end='')
            i += 1
        if i == size:
            break
    elif S[i] == ' ':
        while (stack):
            print(stack.pop(), end='')
        print(' ', end='')
    else:
        stack.append(S[i])
    i += 1
while stack:
    print(stack.pop(), end='')
