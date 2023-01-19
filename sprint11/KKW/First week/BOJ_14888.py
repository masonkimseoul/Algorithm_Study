import math
from itertools import permutations

N=int(input())
num_arr=list(map(str,input().split()))
operator_count=list(map(int,input().split()))
operator={0:'+', 1:'-', 2:'*', 3:'/'}
operator_list=[]

for i in range(4):
    if operator_count[i]!=0:
        for j in range(operator_count[i]):
            operator_list.append(operator[i])

available_operator=set(permutations(operator_list,N-1))
max,min=-math.inf,math.inf

for i in available_operator:
    i=list(i)
    stack=[]
    for j in range(N):
        stack.append(num_arr[j])
        if len(stack)==3:
            temp=int(eval("".join(stack)))
            stack=[str(temp)]
        if j!=N-1:
            stack.append(i[j])
    result=int("".join(stack))
    if result>max:
        max=result
    if result<min:
        min=result
print(max)
print(min)