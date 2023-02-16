import sys

form=sys.stdin.readline().rstrip()
priority={'+':0, '-':0, '*':1, '/':1, '(':-1}
operator=[]
result=''
for c in form:
    if c.isupper():
        result+=c
        continue
    if c=='(':
        operator.append(c)
    elif c==')':
        while operator[-1]!='(':
            result += operator.pop()
        operator.pop()
    else:
        while operator and priority[operator[-1]]>=priority[c]:
            result+=operator.pop()
        operator.append(c)
while operator:
    result+=operator.pop()
print(result)