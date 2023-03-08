import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)
N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
instart = 0
inend = N-1
poststart = 0
postend = N-1
position = [0] * (N+1)
for i in range(N):
    position[inorder[i]] = i


def solution(instart, inend, poststart, postend):
    if (instart > inend) or (poststart > postend):
        return
    root = postorder[postend]

    root_index = position[root]
    left_cnt = root_index-instart
    right_cnt = inend - root_index

    print(root, end=' ')
    solution(instart, instart + left_cnt - 1,
             poststart, poststart + left_cnt - 1)

    solution(inend-right_cnt + 1, inend, postend-right_cnt, postend-1)


solution(instart, inend, poststart, postend)

# 7
# 4 2 5 1 6 3 7
# 4 5 2 6 7 3 1
