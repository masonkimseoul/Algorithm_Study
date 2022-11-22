import sys
# from collections import deque
a, b = map(int, input().split())
graph = [list(map(str,input())) for i in range(a)]
visit = [[0 for _ in range(b)] for _ in range(a)]
def DFS(x,y,px,py,cnt):
  global ans
  if cnt >= 4 and x == px and y == py:
    ans = 1
    return
  nx = [0,0,-1,1]
  ny = [1,-1,0,0]
  for i in range(4):
    dx = nx[i] + x
    dy = ny[i] + y
    if(0<= dx < a and 0 <= dy < b and visit[dx][dy] == 0 and graph[dx][dy] == graph[px][py]):
      visit[dx][dy] = 1
      DFS(dx,dy,px,py,cnt+1)
      visit[dx][dy] = 0

ans = 0
for i in range(a):
  for j in range(b):
    DFS(i,j,i,j,1)
    if(ans == 1):
      print("Yes")
      exit()
if(ans == 0):
  print('No')