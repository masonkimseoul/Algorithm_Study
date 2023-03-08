from itertools import product

def solutions(word):
    vowel=['A','E','I','O','U']
    list=[]
    for i in range(1,6):
        list.extend(map(''.join,product(vowel,repeat=i)))
    list.sort()
    return list.index(word)+1
