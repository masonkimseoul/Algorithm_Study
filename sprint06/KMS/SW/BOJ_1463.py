import sys
sys.setrecursionlimit(100000)
N = int(input())
Memo = [-1 for _ in range(N+1)]
if N <= 1:
    Memo[N] = 0
else:
    Memo[1] = 0
    Memo[2] = 1
for i in range(2,N+1):
    result = []
    if i % 3 == 0:
        result.append(min(Memo[i//3],Memo[i-1])+1)
    if i % 2 == 0:
        result.append(min(Memo[i//2],Memo[i-1])+1)
    result.append(Memo[i-1]+1)
    Memo[i] = min(result)
print(Memo[N])