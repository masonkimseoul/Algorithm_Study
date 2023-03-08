N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))
D = {}

for i in N_list:
    if i in D:
        D[i] += 1
    else:
        D[i] = 1

answer = []
for i in M_list:
    if i in D:
        answer.append(D[i])
    else:
        answer.append(0)
print(*answer)
