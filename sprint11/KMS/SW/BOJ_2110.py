import sys
input = sys.stdin.readline
N, C = map(int, input().split())
L = []
for i in range(N):
    L.append(int(input()))

L.sort()
# 1 2 4 8 9
l = 0
r = L[-1] - L[0]
answer = 0
while l <= r:
    mid = (l+r) // 2
    A = L[0]
    cnt = 1
    for idx, data in enumerate(L[1:]):
        d = data - A
        if d >= mid:
            cnt += 1
            A = data
    if cnt < C:
        r = mid - 1
    else:
        l = mid + 1
print(r)
