import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
result = [-1] * N
stack = []

stack.append(0)
for i in range(1, N):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)

print(result)
print(*result)
