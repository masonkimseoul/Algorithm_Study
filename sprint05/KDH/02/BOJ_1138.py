import sys
input = sys.stdin.readline

N = int(int(input()))

counts = list(map(int, input().split()))
answer = [-1] * N
for i in range(N):
    bigger = (N) - (i+1)

    tmp = 0
    for j in range(N):
        if tmp == counts[i] and answer[j] == -1:
            answer[j] = i+1
            break
        elif answer[j] == -1:
            tmp += 1

print(*answer)
