import sys
input = sys.stdin.readline

n = int(input())
steps = [-1]
for _ in range(n):
    steps.append(int(input()))
dp = [0 for _ in range(n+1)]
# 다이나믹 프로그래밍
# dp[i]란 i층을 오르는데 얻을 수 있는 최대 점수
if n > 3:
    dp[1] = steps[1]
    dp[2] = steps[1] + steps[2]
    dp[3] = steps[3] + max(steps[1], steps[2])

    # 4층 부터는 일관된 규칙이 적용됨 
    for i in range(4, n+1):
        dp[i] = steps[i] + max(dp[i-3]+steps[i-1], dp[i-2])

    print(dp[n])
elif n == 1:
    print(steps[1])
elif n == 2:
    print(steps[1]+steps[2])
elif n==3:
    print(max(steps[1], steps[2]))



