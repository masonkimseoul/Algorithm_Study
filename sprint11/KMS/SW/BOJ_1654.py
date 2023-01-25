K, N = map(int, input().split())
L = []
for i in range(K):
    L.append(int(input()))
l = 1
r = max(L)
answer = 1
while l <= r:
    mid = (l + r) // 2
    cnt = 0
    for i in L:
        cnt += i // mid
    if cnt < N:
        r = mid - 1
    else:
        if answer < mid:
            answer = mid
        l = mid + 1
print(answer)
