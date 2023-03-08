import sys
sys.setrecursionlimit(10000)
T=int(input())

def DFS(arr, x,y,m,n):
    if(x<=-1 or y<=-1 or x>=n or y>=m):
        return False

    if(arr[x][y]==1):
        arr[x][y]=0

        DFS(arr,x,y-1,m,n)
        DFS(arr,x,y+1,m,n)
        DFS(arr,x-1,y,m,n)
        DFS(arr,x+1,y,m,n)

        return True

for i in range(T):
    M,N,K=map(int,input().split(' '))
    cnt=0
    baechuField=[[0]*M for j in range(N)]

    for l in range(0,K):
        X,Y=map(int,input().split(' '))
        baechuField[Y][X]=1

    for a in range(0,N):
        for b in range(0,M):
            if DFS(baechuField,a,b,M,N)==True:
                cnt+=1

    print(cnt)
