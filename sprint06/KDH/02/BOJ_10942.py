import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())

dp =[[0] * N for _ in range(N)]

for move in range(N):
    for start in range(N):
        end = start + move
        if end >= N:
            break
        
        #1
        if start == end:
            dp[start][end] = 1
        elif start + 1 == end:
            if nums[start] == nums[end]:
                dp[start][end] = 1
        else:
            if nums[start] == nums[end] and dp[start+1][end-1] == 1:
                dp[start][end] = 1

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])