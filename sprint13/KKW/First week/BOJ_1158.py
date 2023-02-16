N,K=map(int,input().split())
josephus=list(range(1,N+1))
answer=[]
idx=K-1
while True:
    answer.append(str(josephus[idx]))
    del josephus[idx]
    if len(josephus)==0:
        break
    N-=1
    idx+=(K-1)
    while idx>=N:
        idx-=N
print('<'+", ".join(answer)+">")