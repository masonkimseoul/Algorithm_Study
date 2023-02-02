import sys

def paperCut(x,y,n):
    global papers,minus,zero,plus
    flag=False
    num=papers[y][x]
    for i in range(x,x+n):
        if flag:
            break
        for j in range(y,y+n):
            if papers[j][i]!=num:
                k=n//3
                paperCut(x,y,k)
                paperCut(x+k, y, k)
                paperCut(x+k*2, y, k)
                paperCut(x, y+k, k)
                paperCut(x+k, y+k, k)
                paperCut(x+k*2, y+k, k)
                paperCut(x,y+k*2,k)
                paperCut(x+k, y+k*2, k)
                paperCut(x+k*2, y+k*2, k)
                flag=True
                break
    if not flag:
        if papers[y][x]==-1:
            minus+=1
        elif papers[y][x]==0:
            zero+=1
        else:
            plus+=1


N=int(sys.stdin.readline())
papers=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
minus=0
zero=0
plus=0

paperCut(0,0,N)
print(minus)
print(zero)
print(plus)
