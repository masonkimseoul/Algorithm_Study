N = int(input())
M = [-1] * (N+1)
M[0] = 1
M[1] = 1
def dp(N):
    if M[N] != -1:
        return M[N]
    M[N] = dp(N-1) + dp(N-2) * 2
    return M[N]
if N == 1:
    print(1)
else:
    print(dp(N)%10007)