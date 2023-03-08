from collections import deque
import math
def distance(a,b,c,d):
    return round(math.sqrt((a-c)*(a-c)+(b-d)*(b-d)),2)


def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

N = int(input())
L = []
result = 0
for i in range(N):
    x,y = input().split()
    X = int(float(x) * 100)
    Y = int(float(y) * 100)
    L.append([i,X,Y])
E = []
for i in range(len(L)-1):
    for j in range(i+1,len(L)):
        v,x,y = L[i]
        vv,xx,yy = L[j]
        E.append((v,vv,distance(x,y,xx,yy)))
E.sort(key = lambda x:x[2])

parent = [0] * (len(L))

for i in range(0, len(L)):
	parent[i] = i

for edge in E:
    a, b, cost = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
print(round(result/100,2))
# 3
# 1.0 1.0
# 2.0 2.0
# 2.0 4.0