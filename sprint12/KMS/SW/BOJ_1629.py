# 첫 번째 시도 -> 시간 초과
# import sys
# input = sys.stdin.readline
# A, B, C = map(int, input().split())


# def solution(A, B):
#     if B < 2:
#         return A
#     if B % 2 == 0:
#         A = solution(A, B//2)
#         B = solution(A, B//2)
#     else:
#         A = solution(A, B//2)
#         B = solution(A, B//2+1)
#     return A * B


# print(solution(A, B) % C)
# 두 번째 시도 -> 메모리 초과
# import sys
# input = sys.stdin.readline
# A, B, C = map(int, input().split())
# Memo = [-1]*(B//2 + 2)
# Memo[1] = A
# if B >= 2:
#     Memo[2] = A * A
# if B//2+2 > 3:
#     for i in range(3, B//2 + 2):
#         Memo[i] = Memo[i//2] * Memo[i//2 + 1]
# print(Memo[B//2] * Memo[B//2 + 1] % C)

A, B, C = map(int, input().split())


def solution(A, B, C):
    if B == 1:
        return A % C
    elif B == 2:
        return (A * A) % C
    else:
        if B % 2 == 0:
            return (solution(A, B//2, C) ** 2) % C
        else:
            return (((solution(A, B//2, C) ** 2)) * A) % C


print(solution(A, B, C))
