  
N = int(input())
R = int(input())
L = list(map(int, input().split()))

answer = []
size = 0
while L:
    flag = 0
    tmp = L.pop(0)
    for i in answer:
        if tmp == i[0]:
            i[1] = i[1] + 1
            flag = 1
            break
    if flag == 0:
        if size == N:
            answer.pop(answer.index(min(answer,key = lambda x: x[1])))
            size -=1
        answer.append([tmp,1])
        size+=1
answer.sort(key = lambda x: x[0]) 
for x in answer:
    print(x[0],end = ' ')
