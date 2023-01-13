import itertools
from collections import deque
K = int(input())
Sign_list = list(input().split())
result = []
for h in range(10):
    A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    t = []
    t.append(A.pop(h))
    q = deque()
    q.append((t, A, 0))
    while q:
        k, A, i = q.popleft()
        if i == len(Sign_list):
            result.append(k)
            break
        if Sign_list[i] == '<':
            for idx, data in enumerate(A):
                if k[-1] < data:
                    kk = k[:]
                    kk.append(data)
                    T = A[:]
                    T.pop(idx)
                    q.append((kk, T, i+1))
        else:
            for idx, data in enumerate(A):
                if k[-1] > data:
                    kk = k[:]
                    kk.append(data)
                    T = A[:]
                    T.pop(idx)
                    q.append((kk, T, i+1))

for i in result[0]:
    print(i, end='')
print()
result = []
for h in range(10):
    A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    t = []
    t.append(A.pop(h))
    q = deque()
    q.append((t, A, 0))
    while q:
        k, A, i = q.popleft()
        if i == len(Sign_list):
            result.append(k)
            break
        if Sign_list[i] == '<':
            for idx, data in enumerate(A):
                if k[-1] < data:
                    kk = k[:]
                    kk.append(data)
                    T = A[:]
                    T.pop(idx)
                    q.append((kk, T, i+1))
        else:
            for idx, data in enumerate(A):
                if k[-1] > data:
                    kk = k[:]
                    kk.append(data)
                    T = A[:]
                    T.pop(idx)
                    q.append((kk, T, i+1))
for i in result[0]:
    print(i, end='')
