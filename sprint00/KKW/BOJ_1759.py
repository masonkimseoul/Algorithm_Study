from itertools import combinations
N,M=map(int,input().split())
array=list(map(str,input().split()))
for i in list(combinations(sorted(array),N)):
    vowel=0
    consonant=0
    for j in i:
        if j=='a' or j=='e' or j=='i' or j=='o' or j=='u':
            vowel+=1
        else:
            consonant+=1
    if vowel>0 and consonant>1:
        print("".join(i))