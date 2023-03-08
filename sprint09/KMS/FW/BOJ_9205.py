import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
  n = int(input())
  hx, hy = map(int, input().split())
  store =[]
  for i in range(n):
    sx,sy = map(int,input().split())
    store.append((sx,sy))
  ex,ey = map(int,input().split())

