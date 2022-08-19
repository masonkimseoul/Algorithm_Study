N = int(input())
L =[]
for i in range(N):
    t = int(input())
    flag = 0
    if len(L) <= 1:
        L.append(t)
    else:
        if L[0] > t:
            index = 0
        elif L[-1] < t:
            index = -1
        else:
            for i in range(len(L)-1):
                if L[i] <= t and t <= L[i+1]:
                    index = i+1
        if index == -1:
            L.append(t)
        else:
            L.insert(index,t)
    if len(L) % 2 != 0:
        a = int(len(L)/2)
        print(L[a])
    else:
        a = int(len(L)/2)
        b = a-1
        if L[a] < L[b]:
            print(L[a])
        else:
            print(L[b])
    