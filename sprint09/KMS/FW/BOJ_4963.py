import sys
input = sys.stdin.readline

def dfs(x,y):
  #상 하 좌 우 우상 우하 좌상 좌하
  dy = [1,-1,0,0,1,-1,1,-1]
  dx = [0,0,-1,1,1,1,-1,-1]
  graph[x][y] = 0
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if(0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1):
      dfs(nx,ny)





while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  graph = [list(map(int, input().split())) for _ in range(h)]
  cnt = 0
  for i in range(h):
    for j in range(w):
      if graph[i][j] == 1:
        dfs(i,j)
        cnt+=1
  print(cnt)
