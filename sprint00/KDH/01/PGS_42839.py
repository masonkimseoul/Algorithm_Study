from itertools import permutations

def isPrime(n):  
    if n == 1 or n == 0:
            return False
        
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
def solution(numbers):
    answer = 0
    numbers_ = list(numbers)
    newNumbers = set()
    
    for i in range(len(numbers)):
        for n in list(map(int, map("".join, permutations(numbers_, i+1)))):
            if n not in newNumbers and isPrime(n):
                newNumbers.add(n)
            
    return len(newNumbers)