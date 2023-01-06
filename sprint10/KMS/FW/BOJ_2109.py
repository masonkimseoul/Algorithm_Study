import sys
input = sys.stdin.readline
N = int(input())

arr = []
for i in range(N):
  d, p = map(int, input().split())
  arr.append((d,p))

arr.sort(reverse=True)

check = [0 for _ in range(10001)]
for i in arr:
  d, p = i
  if check[p] == 0:
    check[p] = d
  else:
    for k in range(p-1,0,-1):
      if check[k] == 0:
        check[k] = d
        break
print(sum(check))
