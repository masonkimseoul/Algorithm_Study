import sys

N=int(sys.stdin.readline())
number=list(map(int,sys.stdin.readline().split()))

M=int(sys.stdin.readline())
dp=[0]*(len(number)+1)
for _ in range(M):
    S,E=map(int,sys.stdin.readline().split())
    S-=1
    E-=1
    for i in range(S,E+1):
        end=E-i+S
        if i==end:
            if i==S:
                print(1)
                continue
            else:
                if dp[i-1]==1:
                    print(1)
                    continue
                else:
                    print(0)
                    continue
        if number[i]==number[end]:
            if dp[i]==1:
                continue
            else:
                dp[i]=1
                dp[end]=1
        else:
            print(0)
            continue