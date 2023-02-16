n = int(input())
L = map(str, input().strip())
D = {}
A = ord('A')
for i in range(n):
    D[A] = int(input())
    A += 1

stack = []

for i in L:
    if i == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(b*a)
    elif i == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(b+a)
    elif i == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b/a)
    elif i == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b-a)
    else:
        stack.append(D[ord(i)])

print("%.2f" % stack[0])
