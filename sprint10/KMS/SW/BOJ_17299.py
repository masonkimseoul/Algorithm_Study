import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
D = [0] * 10000000

for i in arr:
    D[i] += 1
result = [-1] * N
stack = []
stack.append(0)
for i in range(1, N):
    while stack and D[arr[stack[-1]]] < D[arr[i]]:
        result[stack.pop()] = arr[i]
    stack.append(i)
print(*result)
