import sys
input = sys.stdin.readline().strip()
N = list(map(int, input))
N.sort(reverse=True)

S = sum(N)
if S % 3 == 0 and N[-1] == 0:
  for i in N:
    print(i,end = '')
else:
  print(-1)


