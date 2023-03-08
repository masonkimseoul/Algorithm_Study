import sys
def palindrome(L):
    if len(L) <= 1:
        return 1
    if L[0] == L[-1]:
        return palindrome(L[1:-1])
    else:
        return 0

N= int(input())
Memo = [[-1] * (N+1) for _ in range(N+1)]
L = list(map(int, sys.stdin.readline().split()))
M = int(input())
for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    # 인덱스이므로 1 빼줌
    a -= 1
    if a+1==b:
        print(1)
    elif a+2 == b:
        if L[a+2] == L[b]:
            print(1)
        else:
            print(0)
    else:            
        if Memo[a][b] != -1:
            print(Memo[a][b])
        else:
            Memo[a][b] = palindrome(L[a:b])
            print(Memo[a][b])