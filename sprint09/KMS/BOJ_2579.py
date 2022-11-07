import sys
input = sys.stdin.readline

n = int(input())
Stairs = [0]
for i in range(n):
  Stairs.append(int(input()))


memo = [[0 for j in range(n+1)] for i in range(3)]

# 0 -> 다음으로 갈 수 있음
# 1 -> 다음으로 못감
# 2 -> 최대값

memo[0][1] = Stairs[1]
memo[2][1] = Stairs[1]


if n >=2:
  memo[0][2] = Stairs[2]
  memo[1][2] = Stairs[2] + Stairs[1]
  memo[2][2] = Stairs[2] + Stairs[1]


for i in range(3,n+1):
  memo[0][i] = Stairs[i] + memo[2][i-2]
  memo[1][i] = Stairs[i] + memo[0][i-1]
  memo[2][i] = max(memo[1][i],memo[0][i])

print(memo[2][n])