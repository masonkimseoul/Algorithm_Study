import sys
import heapq

def calcDistance(a,b):
    if a[0]>b[0]:
        nx=a[0]-b[0]
    else:
        nx=b[0]-a[0]
    if a[1]>b[1]:
        ny=a[1]-b[1]
    else:
        ny=b[1]-a[1]
    return (nx**2+ny**2)**(1/2)

N=int(sys.stdin.readline())
coordinate=[]

for _ in range(N):
    tmpx, tmpy=map(float,sys.stdin.readline().split())
    coordinate.append([tmpx,tmpy])

graph=[[] for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        distance=calcDistance(coordinate[i],coordinate[j])
        graph[i].append([distance,j])
        graph[j].append([distance,i])

answer=0
isVisited=[0]*N
queue=[[0,0]]
while queue:
    distance,node=heapq.heappop(queue)
    if not isVisited[node]:
        isVisited[node]=1
        answer+=distance
        for i in graph[node]:
            heapq.heappush(queue,[i[0],i[1]])
print("%.2f"%answer)