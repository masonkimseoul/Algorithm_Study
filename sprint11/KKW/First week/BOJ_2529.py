import sys
from itertools import permutations

N=int(sys.stdin.readline())
sign=list(sys.stdin.readline().split())
numList=[0,1,2,3,4,5,6,7,8,9]
result=[]
for i in permutations(numList,N+1):
    flag=True
    for j in range(len(sign)):
        if sign[j]=='<':
            if i[j]<i[j+1]:
                continue
            else:
                flag=False
                break
        else:
            if i[j]>i[j+1]:
                continue
            else:
                flag=False
                break
    if flag:
        result.append(i)
print(''.join(list(map(str,max(result)))))
print(''.join(list(map(str,min(result)))))