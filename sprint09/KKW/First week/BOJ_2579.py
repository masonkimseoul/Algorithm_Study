import sys
N=int(sys.stdin.readline())
stairs=[0]
result=[0]*(N+2)
for i in range(N):
    stairs.append(int(sys.stdin.readline()))
stairs.append(0)
result[1]=stairs[1]
result[2]=result[1]+stairs[2]
for i in range(3,N+2):
    result[i]=max(result[i-2],result[i-3]+stairs[i-1])+stairs[i]
print(result[N])
