import sys
N = int(input())

mod = 1000000
p = mod // 10 * 15
Memo = [-1 for i in range(p)]
Memo[0] = 0
Memo[1] = 1
for i in range(2, p):
    Memo[i] = (Memo[i-1] + Memo[i-2]) % mod
print(Memo[N % p])
