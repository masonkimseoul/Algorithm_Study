import sys

N=int(sys.stdin.readline())
cards=[0]+list(map(int,sys.stdin.readline().split()))
answer=[0]*(N+1)
answer[1]=cards[1]

for i in range(2,N+1):
    for j in range(i):
        tmp=answer[j]+cards[i-j]
        if answer[i]<tmp:
            answer[i]=tmp
print(answer[N])