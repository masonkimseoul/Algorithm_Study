import sys
sys.setrecursionlimit(100000)
a, b = map(int, input().split())
# nCr = n!/(n-r)!r!


def two_count(n):
    cnt_two = 0
    while n != 0:
        n = n // 2
        cnt_two += n
    return cnt_two


def five_count(n):
    cnt_five = 0
    while n != 0:
        n = n // 5
        cnt_five += n
    return cnt_five


print(min(two_count(a) - two_count(a-b) - two_count(b),
      five_count(a) - five_count(a-b) - five_count(b)))
