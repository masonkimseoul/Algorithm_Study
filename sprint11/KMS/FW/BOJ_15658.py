import itertools
n = int(input())
L = list(map(int, input().split()))

# 0 -> +
# 1 -> -
# 2 -> *
# 3 -> /

sign_num = list(map(int, input().split()))

R = []


def DFS(plus, minus, mulitple, divide, result, cnt):
    if cnt != n:
        tmp = L[cnt]
        if plus > 0:
            DFS(plus-1, minus, mulitple, divide,
                result+tmp, cnt + 1)
        if minus > 0:
            DFS(plus, minus-1, mulitple, divide,
                result-tmp, cnt + 1)
        if mulitple > 0:
            DFS(plus, minus, mulitple-1, divide,
                result*tmp, cnt + 1)
        if divide > 0:
            if result < 0:
                result *= -1
                result //= tmp
                result *= -1
            elif result == 0:
                result = 0
            else:
                result //= tmp
            # print(result)
            DFS(plus, minus, mulitple, divide-1, result, cnt + 1)
    else:
        R.append(result)


DFS(sign_num[0], sign_num[1], sign_num[2], sign_num[3], L[0], 1)
R.sort()
# print(R)
print(R[-1])
print(R[0])
