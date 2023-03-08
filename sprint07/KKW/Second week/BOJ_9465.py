import sys

T=int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    sticker=[list(map(int,sys.stdin.readline().split())) for __ in range(2)]

    if N==1:
        answer=max(sticker[0][0],sticker[1][0])
    else:
        sticker[0][1]+=sticker[1][0]
        sticker[1][1]+=sticker[0][0]

        for i in range(2,N):
            sticker[0][i]+=max(sticker[1][i-1],sticker[1][i-2])
            sticker[1][i]+=max(sticker[0][i-1],sticker[0][i-2])
        answer=max(sticker[0][N-1],sticker[1][N-1])

    print(answer)