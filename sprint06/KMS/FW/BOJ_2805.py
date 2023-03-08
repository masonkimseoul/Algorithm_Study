import numbers
import sys
N,M = map(int, input().split())
L = list(map(int, sys.stdin.readline().split()))
start, end = 0, max(L)
result = 0
while start <= end:
    take = 0
    mid = (end + start) //2
    for i in L:
        if i > mid:
            take+= i - mid
    if take >= M:
        start = mid +1
        result = mid
    else:
        end = mid -1
print(result)
# 4 7
# 20 15 10 17