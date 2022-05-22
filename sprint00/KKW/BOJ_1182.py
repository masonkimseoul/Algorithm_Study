from itertools import combinations
N,S=map(int,input().split())
motherSet=list(map(int,input().split()))
cnt=0

for i in range(1,N+1):
    subSet=list(combinations(motherSet,i))
    for j in subSet:
        if sum(j)==S:
            cnt+=1

print(cnt)

#5 0
#0 0 0 0 0 을 어떻게 해결할 것인가?
#subSet=set~이 아닌 list~로 해주자