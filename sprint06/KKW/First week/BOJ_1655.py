import sys
import heapq

N=int(sys.stdin.readline())
left=[]
right=[]
for i in range(N):
    tmp=int(sys.stdin.readline())
    if len(left)==len(right):
        heapq.heappush(left,tmp*(-1))
    else:
        heapq.heappush(right,tmp)

    if right and right[0]<left[0]*(-1):
        tmpl=heapq.heappop(left)
        tmpr=heapq.heappop(right)
        heapq.heappush(left,tmpr*(-1))
        heapq.heappush(right,tmpl*(-1))
    print(left[0]*(-1))