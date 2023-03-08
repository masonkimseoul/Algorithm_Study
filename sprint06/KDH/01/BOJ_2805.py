import sys
input = sys.stdin.readline

N, M = map(int, input().split())

trees = list(map(int, input().split()))

start, end = 0, max(trees)


def binary(trees, start, end):
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        tmp = sum(x - mid for x in trees if x > mid)

        if tmp >= M:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    print(ans)


binary(trees, start, end)
