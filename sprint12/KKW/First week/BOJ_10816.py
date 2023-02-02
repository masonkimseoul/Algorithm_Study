import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip().split()))
mn = int(sys.stdin.readline())
ma = list(map(int, sys.stdin.readline().strip().split()))
a.sort()

def fn(arr, ma, s, e):
    if s > e:
        return 0
    m = (s+e)//2
    if arr[m] > ma:
        return fn(arr, ma, s, m-1)
    elif arr[m] < ma:
        return fn(arr, ma, m+1, e)
    else:
        return arr.count(ma)

dic = {}
for i in a:
    if i not in dic:
        dic[i] = fn(a, i, 0, len(a)-1)

print(' '.join(str(dic[x])) if x in dic else '0' for x in ma)