import sys
tmp=sys.stdin.readline()
num=[]
for i in tmp.split('-'):
    result=0
    for j in i.split('+'):
        result+=int(j)
    num.append(result)

answer=num[0]
for i in num[1:]:
    answer-=i
print(answer)