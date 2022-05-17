from itertools import permutations

def isPrime(num):
    if(num<2): return False
    else:
        for i in range(2,num):
            if(num%i==0): return False
        return True

def solution(numbers):
    numNomList=[]
    numList=[]

    for i in range(len(numbers)):
        numNominate=list(map(''.join,permutations(numbers,i+1)))
        for j in numNominate:
            numNomList.append(int(j))

    for i in numNomList:
        if (not i in numList):
            numList.append(i)

    cnt=0
    for i in numList:
        if(isPrime(i)):
            cnt=cnt+1
    return cnt
