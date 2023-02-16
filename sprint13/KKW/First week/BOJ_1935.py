import sys
N=int(sys.stdin.readline())
postfix=list(sys.stdin.readline().rstrip())
numList=[0]*N
stack=[]

for i in range(N):
    numList[i]=int(sys.stdin.readline())
for c in postfix:
    if 'A'<=c<='Z':
        stack.append(numList[ord(c)-ord('A')])
    else:
        num2=stack.pop()
        num1=stack.pop()
        if c=='+':
            stack.append(num1+num2)
        elif c=='-':
            stack.append(num1-num2)
        elif c=='*':
            stack.append(num1*num2)
        elif c=='/':
            stack.append(num1/num2)
print('%.2f' % stack.pop())