N = int(input())
i = 666
cnt = 0
while(True):
    if(str(i).find("666") >= 0):
        cnt = cnt + 1
        if(cnt == N):
            break
    i = i + 1
print(i)