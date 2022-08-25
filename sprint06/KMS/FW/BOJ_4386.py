from collections import deque
import math
def distance(a,b,c,d):
    return round(math.sqrt((a-c)*(a-c)+(b-d)*(b-d)),2)



N = int(input())
L = []
for i in range(N):
    x,y = input().split()
    X = int(float(x) * 100)
    Y = int(float(y) * 100)
    L.append([X,Y])
matrix = [[0 for _ in range(N)] for _ in range(N)]
for i in range(len(L)):
    for j in range(len(L)):
        if i==j:
            continue
        else:
            x,y = L[i]
            xx,yy = L[j]
            matrix[i][j] = distance(x,y,xx,yy)
visit =[0 for _ in range(N)]
S = 0
for i in range(N):
    mind = 0
    save_index = -1
    
    for jinx,j in enumerate(matrix[i]):
        if j == 0:
            continue
        if mind ==0:
            mind = j
        else:
            if mind > j:
                mind = j
                save_index = jinx
    S += mind
print(S)