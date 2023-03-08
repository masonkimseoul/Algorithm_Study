from itertools import *
L,C = map(int, input().split())
list1 = []
list1 = input().split()
list1 = sorted(list1)
for a in combinations(list1,L):
    consonant = 0
    Vowel =0
    for i in a:
        if(i in "aeiou"):
            consonant = consonant + 1
        else:
            Vowel = Vowel + 1
    
    if(consonant >=1 and Vowel >= 2):
        result = ''.join(s for s in a)
        print(result)
