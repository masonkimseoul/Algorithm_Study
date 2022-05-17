N=int(input())
num=666
cnt=0
while cnt<N:
    numStr=str(num)
    for i in range(len(numStr)-2):
        if numStr[i:i+3]=='666':
            cnt+=1
            break
    num+=1
print(num-1)