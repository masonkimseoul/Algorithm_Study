N,M=map(int,input().split())
chess_board=[list(input())for i in range(N)]
cnt=0
min_cnt=N*M
W=list("WBWBWBWB")
B=list("BWBWBWBW")
chess_W=[W,B,W,B,W,B,W,B]
chess_B=[B,W,B,W,B,W,B,W]
for i in range(N-7):
    for j in range(M-7):
        tmp=chess_board[i:i+8]
        for k in range(8):
            tmp[k]=tmp[k][j:j+8]
        for k in range(8):
            for l in range(8):
                if tmp[k][l]!=chess_W[k][l]:
                    cnt+=1
        min_cnt=min(min_cnt,cnt)
        cnt=0
        for k in range(8):
            for l in range(8):
                if tmp[k][l]!=chess_B[k][l]:
                    cnt+=1
        min_cnt=min(min_cnt,cnt)
        cnt=0
print(min_cnt)