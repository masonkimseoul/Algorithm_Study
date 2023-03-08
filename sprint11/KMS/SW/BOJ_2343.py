import sys
input = sys.stdin.readline
N, M = map(int, input().split())
L = list(map(int, input().split()))
start = max(L)
end = sum(L)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    S = 0
    for i in range(N):
        if S + L[i] > mid:
            cnt += 1
            S = 0
        S += L[i]
    if S != 0:
        cnt += 1
    if cnt <= M:
        end = mid - 1
    else:
        start = mid + 1
print(start)
