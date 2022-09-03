import sys


T = int(input())
for i in range(T):
    K = int(input())
    L = []
    L = list(map(int,sys.stdin.readline().split()))
    print(L)
    print(sum(L)/15)