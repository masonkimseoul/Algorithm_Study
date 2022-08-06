from collections import deque

def solution(arr):
    tmp=[]
    arr=deque(arr)
    tmp.append(arr.popleft())
    while arr:
        num=arr.popleft()
        if num!=tmp[-1]:
            tmp.append(num)
    return tmp