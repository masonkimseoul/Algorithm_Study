import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
S = list(map(int, input().split()))
nums = [-1 for _ in range(sum(S))]

for i in range(N):
    combis = list(combinations(S, i+1))
    for c in combis:
        nums[sum(c)-1] = 0

if sum(nums) == 0:
    print(sum(S)+1)
else:
    print(nums.index(min(nums))+1)

