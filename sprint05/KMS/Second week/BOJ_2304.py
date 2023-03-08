N = int(input())
A = []
dict = {}
for i in range(N):
    A.append(list(map(int,input().split())))
    dict[A[-1][0]] = A[-1][1]
A.sort(key = lambda x: -x[0])
start_index = A[-1][0]
end_index = A[0][0]
A.sort(key = lambda x: -x[1])

maxh_index = A[0][0]
H = A[0][1]
# print('start', start_index, 'end', end_index, 'maxh', maxh_index, 'H', H)
sum = 0
height = dict[start_index]
for i in range(start_index,maxh_index):
    if i in dict.keys():
        if dict[i] > height:
            height = dict[i]
    sum += H - height
height = dict[end_index]
for i in range(end_index,maxh_index,-1):
    if i in dict.keys():
        if dict[i] > height:
            height = dict[i]
    sum += H - height
# print(sum)
S = (end_index - start_index+1) * H
print(S - sum)
