N = int(input())
A = []
dict = {}
sum = 0
index = 0
for i in range(N):
    t = int(input())
    sum += t
    A.append(t)
    if t not in dict.keys():
        dict[t] = []
    dict[t].append((1,index))
    index += 1

# # 산술평균
print(round(sum / N))

# #중앙값
A.sort()
print(A[N//2])

#최빈값
Max = 0
maxvalue = 0
for i in dict.keys():
    if Max <= len(dict[i]):
        Max = len(dict[i])
        maxvalue = i
M = []
for i in dict.keys():
    if Max == len(dict[i]):
        M.append(i)
M.sort()
if len(M) > 1:
    print(M[1])
else:
    print(M[0])
    
print(max(A) - min(A))
#