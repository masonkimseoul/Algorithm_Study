from collections import Counter
import sys

N=int(sys.stdin.readline())
numbers=[]
for i in range(N):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

print(round(sum(numbers)/N))
print(numbers[N//2])

cnt=Counter(numbers).most_common()
mostCnt=cnt[0][1]
tmp=[]

for i in cnt:
    if i[1]==mostCnt:
        tmp.append(i)
if len(tmp)!=1:
    tmp.sort()
    print(tmp[1][0])
else:
    print(tmp[0][0])

a=min(numbers)
b=max(numbers)
if a>0 and b>0:
    print(b-a)
elif a<0 and b>0:
    print(b-a)
else:
    print(abs(abs(b)-abs(a)))