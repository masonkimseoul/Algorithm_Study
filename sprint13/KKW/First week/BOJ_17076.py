import sys
def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a

N,S=map(int,sys.stdin.readline().split())
sibling=list(map(int,sys.stdin.readline().split()))

if(len(sibling)==1):
    print(abs(sibling[0]-S))
else:
    for i in range(len(sibling)):
        if(sibling[i]<S):
            sibling[i]=S-sibling[i]
        else:
            sibling[i]-=S
    for i in range(len(sibling)-1):
        answer=gcd(sibling[i],sibling[i+1])
        sibling[i+1]=answer
    print(sibling[-1])