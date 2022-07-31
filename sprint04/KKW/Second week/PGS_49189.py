from collections import deque
from collections import defaultdict

def solution(n,edge):

    dic=defaultdict(list)
    queue=deque([1])
    for i,j in edge:
        dic[i].append(j)
        dic[j].append(i)
    lst = [-1] * (n + 1)
    lst[1]=0

    while queue:
        a=queue.popleft()
        b=lst[a]
        for i in dic[a]:
            if lst[i]==-1:
                queue.append(i)
                lst[i]=b+1
    return len([i for i in lst[1:] if i==max(lst[1:])])