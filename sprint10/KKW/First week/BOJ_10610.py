import sys
num=list(map(str,sys.stdin.readline().rstrip()))

if '0' not in num:
    print(-1)
else:
    result=0
    for i in num:
        result+=int(i)
    if result%3!=0:
        print(-1)
    else:
        for i in sorted(num,reverse=True):
            print(i,end='')