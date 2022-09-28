import sys

N=int(sys.stdin.readline())
S=0

for _ in range(N):
    L=sys.stdin.readline().split()

    if L[0]=="add":
        S |= (1<<int(L[1]))
    elif L[0]=="remove":
        S &= ~(1<<int(L[1]))
    elif L[0]=="check":
        if S & (1<<int(L[1])) !=0:
            print(1)
        else:
            print(0)
    elif L[0]=="toggle":
        S ^=(1<<int(L[1]))
    elif L[0]=="all":
        S = (1<<21)-1
    elif L[0]=="empty":
        S = 0