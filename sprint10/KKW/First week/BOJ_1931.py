import sys
n=int(sys.stdin.readline())
schedule=[list(map(int,sys.stdin.readline().split())) for i in range(n)]
schedule.sort(key=lambda x:[x[1],x[0]])

cnt=0
last=0
for start, end in schedule:
    if start>=last:
        cnt+=1
        last=end
print(cnt)