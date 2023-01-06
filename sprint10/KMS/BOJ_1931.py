import sys
input = sys.stdin.readline
N = int(input())
L = []
for i in range(N):
  start,end = list(map(int,input().split()))
  L.append((start,end))
L.sort(key = lambda x : (x[1],x[0]))
count = 1
start,end = L[0]
ccc = 0
for i in L:
  if ccc == 0:
    ccc+=1
    continue
  tstart,tend = i
  if end <= tstart:
    count+=1
    end = tend
print(count)