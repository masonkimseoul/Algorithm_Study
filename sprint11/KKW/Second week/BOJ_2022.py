import sys
import math
x,y,c=map(float,sys.stdin.readline().split())
l=0
r=min(x,y)
while abs(l-r)>1e-6:
    mid=(l+r)/2
    h1=math.sqrt(x*x-mid*mid)
    h2=math.sqrt(y*y-mid*mid)
    cp=(h1*h2)/(h1+h2)
    if cp>c:
        l=mid
    else:
        r=mid
print("%.3f"%mid)