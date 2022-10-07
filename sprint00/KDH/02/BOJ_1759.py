import sys
input = sys.stdin.readline
from itertools import combinations

L, C = map(int, input().split())
input_ = sorted(list(input().split()))

answer = []

vowel = ['a', 'e', 'i', 'o', 'u']
for combi in list(combinations(input_, L)):
    cnt1 = 0
    cnt2 = 0
    for c in combi:
        if c in vowel:
            cnt1 += 1
        else:
            cnt2 += 1
    if cnt1 >= 1 and cnt2 >= 2:
        answer.append("".join(combi))
        
for a in answer:
    print(a)