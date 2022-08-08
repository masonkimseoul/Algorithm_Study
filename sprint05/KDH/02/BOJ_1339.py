from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
dic = defaultdict()
length = 0
vocabs = []
for _ in range(N):
    vocabs.append(input().rstrip())


for vocab in vocabs:
    for i in range(len(vocab)):
        if vocab[i] not in dic.keys():
            dic[vocab[i]] = 0
        dic[vocab[i]] += 10**(len(vocab) - i - 1)

# 딕셔너리 정렬
dic_ = sorted(dic.items(), key=lambda x: x[1], reverse=True)

answer = 0
num = 9
for d in dic_:
    answer += num * d[1]
    num -= 1
print(answer)
