from collections import deque
n, k = map(int, input().split())

L = deque(i for i in range(1, n+1))
cnt = 0
print('<', end='')
while L:
    t = L.popleft()
    if not L:
        print(t, end='>')
        break
    cnt += 1
    if cnt == k:
        cnt = 0
        print(t, end=', ')
        continue
    L.append(t)
