import math
import sys
sys.setrecursionlimit(10000000)


def isTree(arr, root):
    if arr[root] == '0':
        for i in arr:
            if i == '1':
                return False
    if len(arr) == 1:
        return True
    else:
        return isTree(arr[:root], len(arr[:root])//2) and isTree(arr[root+1:], len(arr[root+1:])//2)


def solution(numbers):
    answer = []
    for i in numbers:
        bs = bin(i)[2:]
        digit = 0
        for i in range(51):
            digit = 2 ** i - 1
            if digit >= len(bs):
                break
        bs = '0' * (digit-len(bs)) + bs
        root = len(bs)//2
        if isTree(bs, root):
            answer.append(1)
        else:
            answer.append(0)
    return answer


solution([1, 1, 1])
