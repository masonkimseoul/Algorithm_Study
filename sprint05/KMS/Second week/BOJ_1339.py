def findindex(L):
    if not L:
        return -1
    max = 0
    cnt = 0
    for i in L:
        tmp = len(i)
        if max < tmp:
            max = tmp
            index = cnt
            
        cnt +=1
    return index

from collections import deque
from string import ascii_uppercase



N = int(input())
result = 0
L = deque()
for i in range(N):
    L.append(input())

alphabet_dict = {}
for i in ascii_uppercase:
	alphabet_dict[i] = 0


for i in L:
    position = 0
    for j in i[::-1]:
        alphabet_dict[j] += 10 ** position
        position += 1
new_dict = sorted(alphabet_dict.items(),key = lambda x : x[1], reverse = True)
L=[]
for value in alphabet_dict.values():
    if value >0:
        L.append(value)
print(L)