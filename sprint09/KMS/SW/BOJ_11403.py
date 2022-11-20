import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr =[]
for i in range(n):
  arr.append(list(map(int,input().split())))
def BFS(idx):
  visit = [0 for _ in range(n)]
  q = deque();
  for i in range(n):
    if arr[idx][i] == 1:
      q.append(i)
  while(q):
    t = q.popleft()
    for i in range(n):
      if arr[t][i] == 1 and visit[i] == 0:
        arr[idx][i] = 1
        visit[i] = 1
        q.append(i)
for i in range(n):
  BFS(i)
for i in range(n):
  for j in range(n):
    print(arr[i][j],end=' ')
  print()


