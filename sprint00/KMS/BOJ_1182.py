from itertools import *
N,S = map(int, input().split())
list1 = map(int, input().split())
list1 = list(list1)
cnt = 0

for i in range(1,N+1):
    for a in combinations(list1, i):
        print(a)
        if(sum(a) == S):
            cnt = cnt+1
print(cnt)
    





    
