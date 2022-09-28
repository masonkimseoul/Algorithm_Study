import sys
from itertools import combinations

N=int(sys.stdin.readline())
sublist=list(map(int,sys.stdin.readline().split()))
sumlist=[]
combilist=[]
t = 0
for i in range(1,N+1):
    combilist=combinations(sublist,i)
    for j in combilist:
        t |= 1 << sum(j)
for i in range(0,t):
    if t & (1 << i) == 1:
        flag = i

# flag=0
#
# if flag==0:
#     print(sumlist[-1]+1)