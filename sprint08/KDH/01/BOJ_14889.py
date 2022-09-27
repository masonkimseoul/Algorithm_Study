from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())

S = []
min_ = 0
for _ in range(N):
    S.append(list(map(int, input().split())))
    min_ += sum(S[_])

teams = list(combinations([i for i in range(N)], N//2))
for i in range(len(teams) // 2):
    team1 = 0
    team2 = 0
    for j in range(N//2-1):
        for k in range(j+1, N//2):
            team1 += S[teams[i][j]][teams[i][k]]
            team1 += S[teams[i][k]][teams[i][j]]
            
            team2 += S[teams[len(teams)-i-1][j]][teams[len(teams)-i-1][k]]
            team2 += S[teams[len(teams)-i-1][k]][teams[len(teams)-i-1][j]]
    min_ = min(min_, abs(team1-team2))
    if min_ == 0:
        break
print(min_)
    