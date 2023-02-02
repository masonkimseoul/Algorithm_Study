import sys

def hanoi1(n,start,tmp,end):
    cnt=0
    if n==1:
        return 1
    else:
        cnt+=hanoi1(n-1,start,end,tmp)
        cnt+=1
        cnt+=hanoi1(n-1,tmp,start,end)
        return cnt

def hanoi2(n,start,tmp,end):
    if n==1:
        print(start,end)
    else:
        hanoi2(n-1,start,end,tmp)
        print(start,end)
        hanoi2(n-1,tmp,start,end)

N=int(sys.stdin.readline())
print("%d"%hanoi1(N,1,2,3))
hanoi2(N,1,2,3)