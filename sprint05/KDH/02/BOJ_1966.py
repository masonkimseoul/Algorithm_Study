# 01
# from collections import deque
# import sys
# input = sys.stdin.readline


# cases = int(input())
# answer = []

# for _ in range(cases):
#     # 개수, 몇 번째
#     N, M = map(int, input().split())
#     rank = list(map(int, input().split()))

#     if N == 1:
#         print(1)
#     else:
#         value_Q = deque(rank)
#         index_Q = deque([i for i in range(N)])

#         cnt = 0
#         while value_Q:
#             if value_Q[0] == max(value_Q):
#                 value_Q.popleft()
#                 idx = index_Q.popleft()
#                 cnt += 1
#                 if idx == M:
#                     print(cnt)
#                     break
#             else:
#                 value_Q.append(value_Q.popleft())
#                 index_Q.append(index_Q.popleft())

# 02
import sys
input = sys.stdin.readline


cases = int(input())
answer = []

for _ in range(cases):
    # 개수, 몇 번째
    N, M = map(int, input().split())
    rank = list(map(int, input().split()))
    idx_ = [i for i in range(N)]

    if N == 1:
        print(1)
    else:
        cnt = 0
        while rank:
            if rank[0] == max(rank):
                rank.pop(0)
                idx = idx_.pop(0)
                cnt += 1
                if idx == M:
                    print(cnt)
                    break
            else:
                rank.append(rank.pop(0))
                idx_.append(idx_.pop(0))
