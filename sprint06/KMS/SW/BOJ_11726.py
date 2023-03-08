N = int(input())
Memo = [-1] * (N+1)
def fibo(N):
    if Memo[N] != -1:
        return Memo[N]
    if N==1:
        Memo[N] = 1
        return 1
    if N==2:
        Memo[N] = 2
        return 2
    Memo[N] = fibo(N-1) + fibo(N-2)
    return Memo[N]

print(fibo(N) % 10007)