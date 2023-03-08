from itertools import combinations
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0
for i in range(N):
    combi = list(combinations(nums, i+1))
    for c in combi:
        if sum(c) == S:
            ans += 1
            
print(ans)
