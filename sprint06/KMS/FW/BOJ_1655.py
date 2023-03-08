N = int(input())
mid = 0
flag = 0
for i in range(N):
    tmp = int(input())
    if i == 0:
        print(tmp)
        mid = tmp
        continue
    # 짝수 일 때
    if i % 2 != 0:
        #상에 들어감
        if mid < tmp:
            flag = 1
        #mid가 상에 들어감
        else:
            mid = tmp
            flag = 1
    # 홀수 일 때
    if i % 2 == 0:
        
    print(mid)
    
    
    
# 6
# 5
# 4
# 4
# 4
# 3
# 3