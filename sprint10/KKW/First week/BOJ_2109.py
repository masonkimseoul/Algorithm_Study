import sys
n=int(sys.stdin.readline())
schedule=[list(map(int,sys.stdin.readline().split())) for i in range(n)]
schedule.sort(key=lambda x:[x[1],x[0]])
plan=[]
deadline=1
result=0
for i in schedule:
    if deadline==i[1]:
        plan.append(i[0])
    else:
        deadline+=1
        result+=max(plan)
        plan.clear()
print(result)