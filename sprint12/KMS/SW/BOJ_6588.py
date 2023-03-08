import sys
input = sys.stdin.readline


def prime_list(n):
    sieve = [True] * n
    for i in range(2, 1001):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return sieve


prime_list = prime_list(1000001)
size = len(prime_list)-1
while True:
    N = int(input())
    flag = 0
    if N == 0:
        break
    for i in range(3, size):
        if prime_list[i] and prime_list[N-i]:
            print(N, '=', i, '+', N-i)
            flag = 1
            break
    if flag == 0:
        print("Goldbach's conjecture is wrong.")
