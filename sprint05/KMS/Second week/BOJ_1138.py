N = int(input())
A = list(map(int, input().split()))
answer = []
for i in range(N):
    answer.append(0)
cnt = 1

while A:
    tmp = A[0]
    del A[0]
    index = 0
    zero_count = 0
    while True:
        if answer[index] == 0:
            if zero_count == tmp:
                answer[index] = cnt
                cnt+=1
                break
            zero_count += 1
        index += 1
for i in answer:
    print(i)