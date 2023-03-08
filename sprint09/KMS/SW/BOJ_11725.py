import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = dict()
for i in range(n-1):
  a,b = map(int,input().split())
  if a not in arr.keys():
        arr[a] = [b]
  else:
      arr[a].append(b)
  if b not in arr.keys():
      arr[b] = [a]
  else:
      arr[b].append(a)

result = dict()
q = deque()
q.append((1,arr[1]))
visited = set()
visited.add(1)
while q:
  parent, child = q.popleft()
  for i in child:
    if i not in visited:
      q.append((i,arr[i]))
      result[i] = parent
      visited.add(i)


for i in range(2,n+1):
  print(result[i])
