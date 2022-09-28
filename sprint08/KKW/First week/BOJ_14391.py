import sys

N,M=map(int,sys.stdin.readline().split())
paper=[list(sys.stdin.readline().rstrip()) for i in range(N)]

answer=0
for i in range(1<<N*M):
    total=0
    for row in range(N):
        rowSum=0
        for col in range(M):
            idx=row*M+col
            if i&(1<<idx)!=0:
                rowSum=rowSum*10+int(paper[row][col])
            else:
                total+=rowSum
                rowSum=0
        total+=rowSum

    for col in range(M):
        colSum=0
        for row in range(N):
            idx=row*M+col
            if i&(1<<idx)==0:
                colSum=colSum*10+int(paper[row][col])
            else:
                total+=colSum
                colSum=0
        total+=colSum

    answer=max(answer,total)
print(answer)