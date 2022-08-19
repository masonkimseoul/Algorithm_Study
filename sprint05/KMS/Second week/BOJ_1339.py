from string import ascii_uppercase
import copy
N = int(input())
result = 0
L = []
for i in range(N):
    L.append(list(input()))
alphabet_dict = {}
for i in ascii_uppercase:
	alphabet_dict[i] = 0
for i in L:
    position = 1
    for j in i[::-1]:
        alphabet_dict[j] += (10 ** position)
        position +=1
num = 9
print(alphabet_dict)
for a,b in sorted(alphabet_dict.items(),key = lambda x: -x[1]):
    if b == 0:
        break
    else:
        alphabet_dict[a] = num
        num-=1
for i in L:
    position = 0
    for j in i[::-1]:
        result += alphabet_dict[j] * (10 ** position)
        position +=1
print(result)