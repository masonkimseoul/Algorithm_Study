import sys
from collections import deque
w,h=map(int,sys.stdin.readline().split())
dx=[0,0,1,-1,1,1,-1,-1]
dy=[1,-1,0,0,1,-1,1,-1]
while(w!=0 and h!=0):
    islandMap=[list(map(int,sys.stdin.readline().split())) for i in range(h)]
    isVisited=[[0 for i in range(w)] for j in range(h)]
    i=0
    j=0
    cnt=0
    indexQueue=deque()
    for i in range(h):
        for j in range(w):
            if islandMap[i][j]==1 and isVisited[i][j]==0:
                isVisited[i][j]=1
                indexQueue.append([i,j])
                while indexQueue:
                    index=indexQueue.popleft()
                    for k in range(8):
                        x=index[0]+dx[k]
                        y=index[1]+dy[k]
                        if x>=0 and x<h and y>=0 and y<w and isVisited[x][y]==0 and islandMap[x][y]==1:
                            isVisited[x][y]=1
                            indexQueue.append([x,y])
                cnt+=1
    print(cnt)
    w,h=map(int,sys.stdin.readline().split())