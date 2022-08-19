from dis import dis
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
line = []
print(L)
for i in range(len(L)-1):
    for j in range(i+1,len(L)):
        line.append(distance(L[i][0],L[i][1],L[j][0],L[j][1]))
print(line)