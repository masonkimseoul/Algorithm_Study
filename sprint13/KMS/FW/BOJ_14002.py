n = int(input())
L = list(map(int, input().split()))
Memo = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if L[j] < L[i]:
            Memo[i] = max(Memo[i], Memo[j] + 1)

ans1 = max(Memo)
ans2 = []
idx = Memo.index(ans1)
cnt = ans1
while idx >= 0:
    if Memo[idx] == cnt:
        ans2.append(L[idx])
        cnt -= 1
    idx -= 1
print(ans1)
ans2.reverse()
print(*ans2)

# 7
# 1 5 6 2 3 4 7
